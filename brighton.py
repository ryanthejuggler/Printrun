#!/usr/bin/python
from bottle import route, run, static_file
import printcore

# sudo pip install bottle
# sudo pip install gevent-websocket

@route('/')
def index():
	return static_file('index.html','static')

@route('/static/<filename>')
def serve_static(filename):
	return static_file(filename,'static')

run(host='0.0.0.0', port=8080, debug=True)
