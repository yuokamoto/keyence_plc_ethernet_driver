#!/usr/bin/env python
#KV8000 upper link
import socket

class PLCSocket(object):
	def __init__(self, host='localhost', port=8501, udp=False):
		self._host = host
		self._port = port
		self._client = None
		self._udp = udp

	def setHost(self, host='localhost', port=8501):
		self._host = host
		self._port = port		

	def connect(self):
		if self._udp:
			self._client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		else:
			self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self._client.connect((self._host, self._port))
			print('Connected to '+self._host+':'+str(self._port))
		except socket.error:
			print('Connection Error to '+self._host+':'+str(self._port))

	def send(self, msg, buff=1024):
		msg = (msg + '\r').encode('utf-8')
		self._client.sendall(msg)
		return self._client.recv(buff).decode('utf-8')
