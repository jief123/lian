#!/usr/bin/env python
# -*- coding: utf-8 -*-           

import web                        

def midd(app):
    """函数规则定义的中间件"""
    def inapp(e, o):
        print 'func befor handle'
        r = app(e, o)
        print 'func after handle'
        return r
    return inapp                  

class Midd(object):
    """class规则定义的中间件,
    其实这就是一个函数,
    传入参数时调用__init__,
    然后返回self"""
    def __init__(self, app):
        self.app = app
    def __call__(self, o, e):
        print 'class befor handle'
        print web.ctx
        r = self.app(o, e)
        print 'class after handle'
        return r                  

def my_processor(handler):
    print 'hook before handling'
#    print web.ctx
    result = handler()
    print result
    print 'hook after handling'
    return result
urls = ("/.*", "hello")
app = web.application(urls, globals())
app.add_processor(my_processor)       

class hello:
    def GET(self):
        print 'start handle'
        return 'Hello, world!\n'      

if '__main__' == __name__:
    app.run(Midd)    #使用class中间件
    #app.run(midd)   #使用函数中间件
