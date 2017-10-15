from socket import *
from multiprocessing import Process
import re

HTML_ROOT_DIR="./html"

def handle_client(client_socket):
	request_data=client_socket.recv(1024)
	#print("request_data:",request_data)
	'''responst_start="HTTP/1.1 200 OK\r\n"
	responst_heders="Server:My sever\r\n"
	responst_body="<html>hello incast</html>"
	response=responst_start+responst_heders+"\r\n"+responst_body
	print("response data:",response)
	client_socket.send(bytes(response,"utf-8"))
	print("success")
	client_socket.close()'''
	request_lines=request_data.splitlines()
	for line in request_lines:
		print(line)
	request_start_line=request_lines[0]  #markkkkkkkkkkkkkk
	file_name=re.match(r"\w+ +(/[^ ]*) ",request_start_line.decode("utf-8")).group(1)
	#if "/"==file_name:
		#file_name="/index.html"
	file_name="index.html"
	try:
		file=open(file_name,"rb")
	except IOError:
		responst_start="HTTP/1.1 404 Not Found\r\n"
		responst_heders="Server:My sever\r\n"
		responst_body="the file is not found!"
	else:
		file_data=file.read()
		file.close()
		responst_start="HTTP/1.1 200 OK\r\n"
		responst_heders="Server:My sever\r\n"
		responst_body=file_data.decode("utf-8")
	response=responst_start+responst_heders+"\r\n"+responst_body
	client_socket.send(bytes(response,"utf-8"))
	client_socket.close()


def main():
	ser_socket=socket(AF_INET,SOCK_STREAM)
	ser_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	ser_socket.bind(("",7888))
	ser_socket.listen(128)
	while True:
		client_socket,client_adress=ser_socket.accept()
		print("[%s,%s]"%(client_adress))
		handle_process=Process(target=handle_client,args=(client_socket,))
		handle_process.start()
		client_socket.close()



if __name__ == '__main__':
	main()