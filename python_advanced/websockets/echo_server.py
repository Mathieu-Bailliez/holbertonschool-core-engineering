#!/usr/bin/env python3
"""WebSocket echo server that sends back every message it receives."""


import asyncio

from websockets.asyncio.server import serve


async def echo(websocket):
    """Send back every message it receives."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the echo server and keep it running forever."""
    async with serve(echo, "127.0.0.1", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
