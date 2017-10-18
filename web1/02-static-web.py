from socket import *
from multiprocessing import Process
import re
import sys
wsgi_dir="./wsgipython"
HTML_ROOT_DIR="./html"

class HTTPServer(object):
	
	def __init__(self):
		self.ser_socket=socket(AF_INET,SOCK_STREAM)
		self.ser_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	def start(self):
		self.ser_socket.listen(128)

		while True:
			client_socket,client_adress=self.ser_socket.accept()
			print("[%s,%s]"%(client_adress))
			handle_process=Process(target=self.handle_client,args=(client_socket,))
			handle_process.start()
			client_socket.close()
	def start_response(self,status,headers):
		#server_headers={("server","my sever")}
	 	#server_headers+headers
	 	response_headers="HTTP/1.1 "+status+"\r\n"
	 	for header in headers:
	 		response_headers+="%s: %s\r\n" % header
	 	self.response_headers=response_headers
	def handle_client(self,client_socket):
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
		#for line in request_lines:
			#print(line)
		request_start_line=request_lines[0]  #markkkkkkkkkkkkkk
		'''print("***********")
		print(request_start_line)
		print("***********")'''
		file_name=re.match(r"\w+ +(/[^ ]*) ",request_start_line.decode("utf-8")).group(1)
		b=".py"
		'''print("***********")
		print(file_name)
		print("***********")'''
		#print(b)
		#print(file_name)
		if str(file_name).endswith(b):
			m=__import__(file_name[1:-3])
			env={}
			response_body=m.application(env,self.start_response)
			response=self.response_headers+"\r\n"+response_body



		else:
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
		#response=responst_start+responst_heders+"\r\n"+responst_body
		client_socket.send(bytes(response,"utf-8"))
		client_socket.close()
	def bind(self,port):
		self.ser_socket.bind(("",port))
def main():
	sys.path.insert(1,wsgi_dir)
	http_sever=HTTPServer()
	http_sever.bind(7788)
	http_sever.start()

	


if __name__ == '__main__':
	main()