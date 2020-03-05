import sys, socket, threading
import tincanchat

HOST = sys.argv[-1] if len(sys.argv) > 1 else '127.0.0.1'
PORT = tincanchat.PORT

def handle_input(sock):
	"""Prompt user for message and send it too server"""
	print("Type messages, enter to send. 'q' to quit")
	while True:
		msg = input()
		if msg == 'q':
			sock.shutdown(socket.SHUT_RDWR)
			sock.close()
			break
		try:
			tincanchat.send_msg(sock, msg)
		except(BrokenPipeError, ConnectionError):
			break

if __name__ == '__main__':
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, PORT))
	print('COnnected to {}:{}'.format(HOST, PORT))

	thread = threading.Thread(target=handle_input,
	args=[sock],
	daemon=True)
	thread.start()
	rest=bytes()
	while True:
		try:
			(msgs, rest) = tincanchat.recv_msgs(sock, rest)
			for msg in msgs:
				print(msgs)
				print(msg)
		except ConnectionError:
			print('Connection to server closed')
			sock.close()
			break
