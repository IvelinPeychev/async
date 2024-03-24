import asyncio
import pytest

# Mock I/O operation coroutine
async def async_io_operation(mock_data):
    await asyncio.sleep(1)  # Simulate I/O delay
    return mock_data * 2

# The test for the coroutine's functionality
@pytest.mark.asyncio
async def test_async_io_operation():
    input_data = 10
    expected_result = input_data * 2
    result = await async_io_operation(input_data)
    assert result == expected_result, "The coroutine did not return the expected result."
