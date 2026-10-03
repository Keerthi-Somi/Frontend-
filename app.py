from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = """
        <html>
        <head>
            <title>Python Deployment</title>
        </head>
        <body>
            <h1>Python Application Deployed Successfully!</h1>
            <p>Jenkins + Docker deployment is working.</p>
        </body>
        </html>
        """

        self.wfile.write(message.encode())


server = HTTPServer(("0.0.0.0", 80), MyHandler)

print("Python server running on port 80...")

server.serve_forever()
