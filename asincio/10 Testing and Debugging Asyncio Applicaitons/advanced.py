import asyncio
import pytest
import time


# Coroutine that deliberately takes longer than expected
async def long_running_task():
    await asyncio.sleep(2)  # Longer running task
    return "Long task completed"


# Coroutine with a normal operation time
async def quick_task():
    await asyncio.sleep(0.1)  # Quick task
    return "Quick task completed"


# Complex workflow that involves multiple tasks
async def complex_workflow():
    start_time = time.time()
    long_task = asyncio.create_task(long_running_task())
    quick_task_1 = asyncio.create_task(quick_task())
    quick_task_2 = asyncio.create_task(quick_task())

    # Simulate some additional async operations here if needed
    # ...

    # Wait for all tasks to complete
    results = await asyncio.gather(long_task, quick_task_1, quick_task_2)
    end_time = time.time()

    # Check for task completion timing issues
    assert end_time - start_time < 3, "Workflow took too long to complete"
    return results


# The test for the complex workflow debugging scenario
@pytest.mark.asyncio
async def test_complex_workflow():
    # Enable asyncio debug mode
    asyncio.get_event_loop().set_debug(True)

    results = await complex_workflow()

    # Debugging: printing results or any debug info if needed
    # For real-world debugging, you would inspect these results,
    # asyncio debug logs, or utilize breakpoints.
    print(results)

    # Assertions to validate the results can be added here
    assert "Long task completed" in results
    assert results.count("Quick task completed") == 2
