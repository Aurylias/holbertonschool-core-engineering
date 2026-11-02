#!/usr/bin/env python3
"""An echo server with message validation"""

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


async def echo(websocket):
    try:
        async for message in websocket:
            if message.isspace() or message == "":
                await websocket.send('ERR:EMPTY')
            else:
                await websocket.send(f'OK:{message}')
    except ConnectionClosed:
        pass


async def main():
    async with serve(echo, '127.0.0.1', 8765):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
