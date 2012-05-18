#!/usr/bin/python
import sys
# append facerec to module search path
sys.path.append("../..")
import cv2
from facedet.detector import SkinFaceDetector
import numpy as np
import os


def extract_faces(src, dst, detector, face_sz = (200,200)):
	"""
	Extracts the faces from all images in a given src_dir and writes the extracted faces
	to dst_dir. Needs a facedet.Detector object to perform the actual detection.
	
	Args:
		src_dir [string] 
		dst_dir [string] 
		detector [facedet.Detector]
		face_sz [tuple] 
	"""
	src_fn = src
        print(src_fn) 
        img = cv2.imread(src_fn)
	rects = detector.detect(img)
	for i,rect in enumerate(rects):
		print "caonima"
		x0,y0,x1,y1 = rect
		face = img[y0:y1,x0:x1]
		face = cv2.resize(face, face_sz, interpolation = cv2.INTER_CUBIC)
		cv2.imwrite(dst, face)

if __name__ == "__main__":
	src = "/root/img/subfj/20120515_152424.jpg" 
	dst = "/tmp/2012.jpg" 
	detector = SkinFaceDetector(threshold=0.01, cascade_fn="/root/libface/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml")
	extract_faces(src=src, dst=dst, detector=detector)
