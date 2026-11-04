#!/usr/bin/env python3
"""WebSocket server that validates each message before replying."""

import asyncio

from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


async def validate(websocket):
    """Reply to each message from one client."""
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                response = "ERR:EMPTY"
            else:
                response = f"OK:{message}"
            await websocket.send(response)
    except ConnectionClosed:
        pass


async def main():
    """Start the validation server and keep it running forever."""
    async with serve(validate, "127.0.0.1", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
