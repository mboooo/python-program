import urllib.request  
import urllib  
import gzip  
import http.cookiejar  
import os
from tkinter import *
import tkinter.messagebox
import base64

#定义一个方法用于生成请求头信息，处理cookie  
def getOpener(head):  
	# deal with the Cookies   
	cj = http.cookiejar.CookieJar()  
	pro = urllib.request.HTTPCookieProcessor(cj)  
	opener = urllib.request.build_opener(pro)  
	header = []  
	for key, value in head.items():  
		elem = (key, value)  
		header.append(elem)  
	opener.addheaders = header  
	#print(header)
	return opener  
  
#定义一个方法来解压返回信息  
def ungzip(data):  
	try:        # 尝试解压  
		print('正在解压.....')  
		data = gzip.decompress(data)  
		print('解压完毕!')  
	except:  
		print('未经压缩, 无需解压')  
	return data  
# id="a"
# password="a"


def a():
	
	id=t1.get()
	password=t2.get()
	if id=='' or password=='':
		tkinter.messagebox.showinfo(title="message",message="用户名或密码为空")
		return
	try:
		global header
		# global id
		# global password
		opener = getOpener(header)  

		url = 'http://1.1.1.2/ac_portal/login.php'  


		opr='pwdLogin'
		rememberPwd=0
		postDict = {  
				'userName': id.strip(),  
				'pwd': password.strip(),  
				'opr':opr,
				'rememberPwd':rememberPwd,
		}  





		postData = urllib.parse.urlencode(postDict).encode()  
		op = opener.open(url, postData)  
		data = op.readline()
		# data = ungzip(data)  
		
		ff=open(r"D:\login\info.txt","w")
		#print("1111111")
				
		ff.writelines(id+"\n")
		ff.writelines(password)
		ff.close()
		msg=str(data,encoding="UTF-8")
		b=msg.split(',',6)
		# print(b[1])
		# c=b.split(':',2)
		# print(c[1])
		c=b[0].split(':',2)
		# print(c[1])
		m=b[1].split(':',2)
		d=c[1]
		f=d[1:-1]
		tip=m[1]
		top=tip[1:-1]
		if c[1]=="success":
			# print("success")
			tkinter.messagebox.showinfo(title="message",message=top)
		elif c[1]=="false":
			if top=="用户已在线，不需要再次认证":
				print(top)
				tkinter.messagebox.showinfo(title="message",message=top)
			elif top=="用户名或密码错误":
				print(top)
				tkinter.messagebox.showinfo(title="message",message=top)
			else:
				print("Error")
				tkinter.messagebox.showinfo(title="message",message=top)


		# print(f)#最终分割出来的结果msg:
		# label=Label(root,text=f).pack()
		# Message("asdf")
		# tkinter.messagebox.showinfo(title="message",message=f)
	except:
		# tkinter.messagebox.showinfo(title="Error",message="Error")
		tkinter.messagebox.showinfo(title="message",message="Error:002")

header={
#"POST /ac_portal/login.php HTTP/1.1",
'Host': '1.1.1.2',
'Connection': 'keep-alive',
'Content-Length': '65',
'Accept': '*/*',
'Origin': 'http://1.1.1.2',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Referer': 'http://1.1.1.2/ac_portal/default/pc.html?tabs=pwd',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',

}



	
	

if __name__ == '__main__':
	root=Tk()
	root.title('login v1.0')
	# root.geometry('250x150')
	id=""
	password=""
	t1=StringVar()
	t2=StringVar()
	if(os.path.exists(r"D:\login\info.txt")):
		ff=open(r"D:\login\info.txt")
		id=ff.readline()
		password=ff.readline()
		# passworda=ff.readline()
		# id=base64.decodestring(ida)
		# password=base64.decodestring(password)
		# print(id.strip())
		# print(password.strip())
		ff.close()
	else:
		try:
			if os.path.exists(r"D:\login"):
				ff=open(r"D:\login\info.txt")
				ff.close()
			else:
				os.mkdir("D:\login")
				ff=open(r"D:\login\info.txt")
				ff.close()
		except:
			# tkinter.messagebox.showinfo(title="message",message='Error:001')
			pass
			# ff=open(r"D:\login\info.txt","w")
			# ff.close()
			
			# t1.set=(" ")
		ff=open(r"D:\login\info.txt","w")
		ff.close()
	if(os.path.exists(r"D:\login\info.txt")):
		t1.set(id.strip())
		t2.set(password.strip())
	entry1=Entry(root,textvariable=t1,width=30).pack()
	entry2=Entry(root,textvariable=t2,width=30).pack()
	btn=Button(root,text='sign in',command=a,width=30)
	btn.pack()
	root.mainloop()
	
	# print("a")