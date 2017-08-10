#!/usr/bin/python2.7

import time
import BaseHTTPServer
import textwrap
import re


HOST_NAME = 'localhost'
PORT_NUMBER = 8004


def status_Code_Helper(path):
    path = path.split('?', 1)[0]
    if path in {'/accept', '/success'}:
        return 200
    elif path in {'/reject', '/fail'}:
        return 500
    elif path == '/':
        print("Enter status code to return:")
        return input()
    elif re.match('/[2-5]\d\d', path):
        return int(path[1:4])
    else:
        return 404

def header_Helper(s, status):
    s.send_response(status)
    s.send_header("Content-type", "text/html")
    s.end_headers()


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        status = status_Code_Helper(s.path)
        header_Helper(s, status)
    def do_GET(s):
        status = status_Code_Helper(s.path)
        header_Helper(s, status)
        s.wfile.write("<html><head><title>Ethan's Testing Server</title></head>")
        s.wfile.write("<body><h1>Status Code: %s</h1><p>You've reached Ethan's Test Server. Thanks for using this service.</p>" % status)
        s.wfile.write("<p>You accessed path: '%s' via a GET request</p>" % s.path)
        s.wfile.write("<p>Powered by Python</p></body></html>")
    def do_POST(s):
        status = status_Code_Helper(s.path)
        header_Helper(s, status)
        s.wfile.write("<html><head><title>Ethan's Testing Server</title></head>")
        s.wfile.write("<body><h1>Status Code: %s</h1><p>You've reached Ethan's Test Server. Thanks for using this service.</p>" % status)
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
