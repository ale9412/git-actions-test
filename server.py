import http.server
import socketserver
from http import HTTPStatus
import os

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello my f**king World')
        self.wfile.write(b'Getting color %s from env'%os.getenv("COLOR"))


print("Serving on port 8000")
httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
