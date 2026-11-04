#!/usr/bin/env python3
"""WebSocket client that sends one message and prints the reply."""


import asyncio

from websockets.asyncio.client import connect


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to uri, send text once, and return the reply as a str."""
    async with connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv(decode=True)
        return response


if __name__ == "__main__":
    result = asyncio.run(connect_and_send("ws://127.0.0.1:8765/",
                                          "Hello WebSocket"))
    print(result, end="")
