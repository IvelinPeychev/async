import asyncio
import random

async def stock_data_stream(symbol):
    """Simulate a stream of stock price updates."""
    while True:
        await asyncio.sleep(random.uniform(0.1, 0.5))  # Simulate variable network delay
        price_update = random.uniform(-1, 1)  # Simulate price change
        yield symbol, price_update

async def analyze_price_change(symbol, change):
    """Placeholder function to analyze price change."""
    # Imagine complex analysis here.
    print(f"Analyzed {symbol}: Change {change}")

async def consume_stream(symbol):
    """Consume the stock data stream and process updates as they arrive."""
    async for symbol, change in stock_data_stream(symbol):
        await analyze_price_change(symbol, change)  # Process each update individually.

# Example usage: Start processing real-time data for a stock symbol.
asyncio.run(consume_stream("AAPL"))
