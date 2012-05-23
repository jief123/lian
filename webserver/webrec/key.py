#!/usr/bin/python
i = 1 
class value():
	def __init__(self,x=0):
		self.key = x
		print("class init")
	def setkey(self,x):
		self.key = x
	def getkey(self):
		return self.key
k = value()
