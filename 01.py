from socket import *
from multiprocessing import Process

html_root_dir=""

def handle_client(client_socket):
	request_data=client_socket.recv(1024)
	#print("request_data:",request_data)
	responst_start="HTTP/1.1 200 OK\r\n"
	responst_heders="Server:My sever\r\n"
	responst_body="<html>hello incast</html>"
	response=responst_start+responst_heders+"\r\n"+responst_body
	print("response data:",response)
	client_socket.send(bytes(response,"utf-8"))
	print("success")
	client_socket.close()

def main():
	ser_socket=socket(AF_INET,SOCK_STREAM)
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