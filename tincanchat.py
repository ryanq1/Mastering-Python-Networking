import socket

HOST = ''
PORT = 4040

def create_listen_socket(host, port):
	""" Setup the sockets our server will recieve connection
	requests on"""
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((host, port))
	sock.listen(100)
	return sock

def recv_msg(sock):
	"""Wait for data to arrvie on the socket, then parse into messages using b'\0\ as message delimiter:"""
	data = bytearray()
	msg = ''
	while not msg:
		recvd = sock.recv(4096)
		if not recvd:
			raise ConnectionError()
		data = data + recvd
		if b'\0' in recvd:
			msg = data.rstrip(b'\0')
	msg =msg.decode('utf-8')
	return msg

def prep_msg(msg):
	msg += '\0'
	return msg.encode('utf-8')

def send_msg(sock, msg):
	data = prep_msg(msg)
	sock.sendall(data)
def parse_recvd_data(data):
	parts = data.split(b'\0')
	msgs = parts[:-1]
	rest = parts[-1]
	return(msgs,rest)

def recv_msgs(sock, data=bytes()):
	msgs=[]
	while not msgs:
		recvd = sock.recv(4096)
		if not recvd:
			raise ConnectionError()
		data = data + recvd
		(msgs, rest) = parse_recvd_data(data)
	msg = [msg.decode('utf-8') for msg in msgs]
	return (msgs, rest)
