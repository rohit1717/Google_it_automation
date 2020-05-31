#!/usr/bin/env python3
import requests
from PIL import Image
import os, sys
path = "/home/student-02-af107140b3eb/supplier-data/images/"
dirs = os.listdir( path )



url = "http://localhost/upload/"
for item in dirs:
	if item[4:]=='jpeg':
		with open(path+item, 'rb') as opened:
			r = requests.post(url, files={'file': opened})