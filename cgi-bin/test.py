#!/usr/bin/env python3
#print("Content-Type: text/html\n")
#print("<!doctype html><title>Hello</title><h2>hello world</h2>")

f = open("/home/jorgerkdo/Documents/Python/python_web/cgi-bin/test.txt","w+")
f.write('This is was executed from HTTP Server ')
f.close()