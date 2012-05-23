#!/usr/bin/python
import extract
import reco
#import

#class
class rec:
	def __init__(self):
		self.label="right"
		self.recdb = reco.recdb()
		print("rec init")
	def predict(self,filename_src,filename_dst):
		filename = extract.extract_face(filename_src,filename_dst)
		return self.recdb.recpeo(filename)
	def train(self,filename,label):
		return

r = rec()
