#!/usr/bin/python2.7

import time
import BaseHTTPServer
import textwrap


HOST_NAME = 'localhost'
PORT_NUMBER = 8004


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        if s.path == '/accept':
            s.send_response(200)
        elif s.path == '/fail':
            s.send_response(500)
        else:
            s.send_response(404)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        if s.path == '/accept':
            s.send_response(200)
        elif s.path == '/fail':
            s.send_response(500)
        else:
            s.send_response(404)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write("404: Page Not Found")
            return
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Ethan's Testing Server</title></head>")
        s.wfile.write("<body><p>You've reached Ethan's Test Server. Thanks for using this service.</p>")
        s.wfile.write("<p>You accessed path: '%s' via a GET request</p>" % s.path)
        s.wfile.write("<p>Powered by Python</p></body></html>")
    def do_POST(s):
        if s.path == '/accept':
            s.send_response(200)
        elif s.path == '/fail':
            s.send_response(500)
        else:
            s.send_response(404)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write("404: Page Not Found")
            return
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Ethan's Testing Server</title></head>")
        s.wfile.write("<body><p>You've reached Ethan's Test Server. Thanks for using this service.</p>")
        data = s.rfile.read(int(s.headers['Content-Length']))
        s.wfile.write("<p>You sent data: %s</p>" % data)
        wrapper = textwrap.TextWrapper(initial_indent="* ", subsequent_indent="*   ")
        print(wrapper.fill(data))
        s.wfile.write("<p>Powered by Python</p></body></html>")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))
