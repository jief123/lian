#!/usr/bin/python
import web
import key
import os
import time
from lian import *

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
	time.sleep(10)
        return 'Hello, world!'
    def POST(x):
	key.i += 1
	x = web.data()
	print(type(x))
	if os.path.isdir('/tmp/img/extract/'): 
		pass 
	else: 
		os.makedirs('/tmp/img/extract/')
	if os.path.isdir('/tmp/img/upload/'): 
		pass 
	else: 
		os.makedirs('/tmp/img/upload/')
	f = open('/tmp/img/upload/'+str(key.i), 'w')
	f.write(x)
	f.close
	lable = r.predict('/tmp/img/upload/'+str(key.i),'/tmp/img/extract/'+str(key.i))
	return lable 
#	return "yes" 
if __name__ == "__main__":
    key.i = 0
    app.run()
