#import asyncio
#import websockets
#from jsonrpcclient.clients.websockets_client import WebSocketsClient
import websocket
import requests
import _thread
import time
import json


class MoonrakerWebsocket():
    _id = 0
    connected = False

    def __init__(self, host, port):
        self.url = "%s:%s" % (host, str(port))
    
    def connect(self):
        token = self.get_token()
         
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://%s/websocket?token=%s" % (self.url, token),
                on_open=self.on_open,
                on_message=self.on_message,
                on_error=self.on_error,
                on_close=self.on_close)
        self.ws.run_forever()

    def disconnect(self):
        print("Closing socket connection")
        self.ws.close()

    def request_data(self, method, params={}):
        self._id += 1
        data = {
                "jsonrpc": "2.0",
                "method": method,
                "params": params,
                "id": self._id
                }
        self.ws.send(json.dumps(data))

    def get_token(self):
        try:
            response = requests.get("http://%s/access/oneshot_token" % self.url).json()
            return response["result"]
        except:
            print("Unable to retrive oneshot token")
            return None

    def on_message(self, ws, message):
        response = json.loads(message)
        print("Got message")
        print(response)
        return 

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print("## CLOSED ##")

    def on_open(self, ws):
        def run(*args):
            self.request_data("printer.info")
            #self.ws.request("printer.info")
            self.ws.close()
            print("thread terminating...")
        _thread.start_new_thread(run, ())




if __name__ == "__main__":
    #websocket.enableTrace(True)
    #ws = websocket.WebSocketApp("ws://192.168.1.166:7125/websocket?token=%s" % get_token(),
    #        on_open=on_open,
    #        on_message=on_message,
    #        on_error=on_error,
    #        on_close=on_close)
    #ws.run_forever()
    moonrakerSocket = MoonrakerWebsocket("192.168.1.166", 7125)
    moonrakerSocket.connect()

#async def main():
#    async with websockets.connect("ws://192.168.1.166:7125/websocket?token=%s" % get_token()) as ws:
#        response = await WebSocketsClient(ws).request("printer.info")
#    print(response.data.result)

#asyncio.get_event_loop().run_until_complete(main())


