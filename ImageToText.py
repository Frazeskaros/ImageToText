#!/usr/bin/python
import os
import sys

path = input("Select the path \n> ")
	
f=os.listdir(path)
for file in f:
	new_path=path+file
	print("OCR> "+new_path)
	os.system("tesseract "+new_path+" "+file+" --dpi 150")
