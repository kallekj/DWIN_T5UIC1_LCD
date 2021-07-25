import asyncio
import websockets
from jsonrpcclient.clients.websockets_client import WebSocketsClient
import requests
import json

def get_token():
    response = requests.get("http://192.168.1.166:7125/access/oneshot_token").json()
    print(response["result"])
    return response["result"]

async def main():
    async with websockets.connect("ws://192.168.1.166:7125/websocket?token=%s" % get_token()) as ws:
        response = await WebSocketsClient(ws).request("printer.info")
    print(response.data.result)

asyncio.get_event_loop().run_until_complete(main())
