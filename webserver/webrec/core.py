#!/usr/bin/python
import web

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hello, world!'
    def POST(x):
	x = web.data()
	f = open('/tmp/img/upload/jpgfile', 'w')
	f.write(x)
	return 'yes'
if __name__ == "__main__":
    app.run()
