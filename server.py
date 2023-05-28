import http.server
import socketserver
from http import HTTPStatus
import os

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(b'Hello my f**king World\n')
            string = 'Getting color %s from env'%os.getenv("COLOR")
            self.wfile.write(bytes(string, "utf-8"))
        except KeyboardInterrupt:
            self.close()

print("Serving on port 8000")
httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
