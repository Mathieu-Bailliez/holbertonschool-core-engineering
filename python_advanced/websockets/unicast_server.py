#!/usr/bin/env python3
"""WebSocket server that replies only to the client who sent the message."""


import asyncio

from websockets.asyncio.server import serve

connected_clients = set()


async def unicast_handler(websocket):
    """Track the connection and send each message back with a 'U:' prefix."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the server on 127.0.0.1:8765 and keep it running."""
    async with serve(unicast_handler, "127.0.0.1", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
