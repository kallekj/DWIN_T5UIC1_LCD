from jsonrpcclient.clients.http_client import HTTPClient
import jsonrpclib
import socket
import requests
import json




class moonrakerClient:
	def __init__(self, address, port):
		self.client = HTTPClient('%s' % (address))

class moonrakerClientV2:
	def __init__(self, address, port):
		self.client = jsonrpclib.Server('%s:%s' % (address, str(port)))


def main():
    #print(jsonrpclib.config.version)
    #moonraker_rpc_v2 = moonrakerClientV2("192.168.1.166", 7125)
    #moonraker_rpc_v2.client._request("info", {}, rpcid=1)
    #moonraker_rpc = moonrakerClient("http://192.168.1.166", 7125)
    #pinter_obj = moonraker_rpc.client.send('{"jsonrpc": "2.0", "method": "printer.info", "params":{}, "id": 1}')
    #moonraker = moonrakerSocket("http://192.168.1.166", 7125)
    #moonraker.s.send("/printer/info")
    url = "http://192.168.1.166:7125"

    # Example echo method
    payload = {
        "method": "printer.info",
        "params": {},
        "jsonrpc": "2.0",
        "id": 1234,
    }
    response = requests.get(url, json=payload)
    print(response)

    response = requests.get(url + "/printer/info")
    print(response)

if __name__ == "__main__":
    main()

