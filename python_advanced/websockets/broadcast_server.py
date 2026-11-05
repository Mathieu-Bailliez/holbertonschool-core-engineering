#!/usr/bin/env python3
"""Broadcast WebSocket server that relays every message to all clients."""

import asyncio

from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def send_to_all(text):
    """Send the text to every connected client."""
    for ws in connected_clients.copy():
        try:
            await ws.send(text)
        except ConnectionClosed:
            connected_clients.discard(ws)


async def broadcast_handler(websocket):
    """Register a client and send each of its messages to every client."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await send_to_all(f"B:{message}")
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the server on 127.0.0.1:8765 and keep it running."""
    async with serve(broadcast_handler, "127.0.0.1", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
