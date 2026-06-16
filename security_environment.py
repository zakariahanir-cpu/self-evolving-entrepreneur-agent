from scapy.all import *
from mitmproxy import ctx, http

class SecurityEnvironment:
    def __init__(self):
        self.scapy_client = scapy.all

    def send_packet(self, packet):
        self.scapy_client.send(packet)

    def manipulate_http_traffic(self, request):
        return http.HTTPResponse.make(
            200,
            b"Hello, world!",
            {"Content-Type": "text/html"},
        )