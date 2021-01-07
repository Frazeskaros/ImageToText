#!/usr/bin/python
import os

opsy= input("Select OS (ubu, fed, man)\n>")

#Ubuntu
if opsy=="ubu": 
	os.system("sudo apt-get install tesseract-ocr")

#Fedora
elif opsy=="fed":
	os.system("sudo dnf install tesseract")

#Manjaro
elif opsy=="man":
	os.system("sudo pacman -Syu tesseract")
