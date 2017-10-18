import time
def application(env,start_reponse):
	status="200 ok"
	headers={
	("Content-Type","text/plain")
	}
	start_reponse(status,headers)
	return time.ctime()