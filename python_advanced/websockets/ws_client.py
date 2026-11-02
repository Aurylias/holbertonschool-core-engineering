#!/usr/bin/env python3
"""Implementtion of a WebSocket client"""
import asyncio
from websockets.asyncio.client import connect


async def connect_and_send(uri: str, text: str) -> str:
    async with connect(uri) as ws:
        await ws.send(text)
        return await ws.recv()


async def main():
    response = await connect_and_send("ws://127.0.0.1:8765", "Hello WebSocket")
    print(response, end="")


if __name__ == '__main__':
    asyncio.run(main())
