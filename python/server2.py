import http.server
import socketserver
import cgitb


'''
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT),Handler) as httpd:
	print ("serving at port",PORT)
	httpd.serve_forever()

cgitb.enable()
#python3 -m http.server --bind localhost --cgi 8000
'''
server_address = ('', 8000)
handler = CGIHTTPServer.CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin']
server = CGIHTTPServer.BaseHTTPServer.HTTPServer(server_address, handler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()