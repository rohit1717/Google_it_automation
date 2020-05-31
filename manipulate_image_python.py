
#!/usr/bin/env python3
from PIL import Image
import os, sys

path = "/home/student-02-af107140b3eb/supplier-data/images/"
dirs = os.listdir( path )

for item in dirs:
	if os.path.isfile(path+item):
		try:
			im = Image.open(path+item)
			imResize = im.resize((600,400))
			imResize.save(path+item[0:-5]+'.jpeg', 'JPEG')
		except:
			pass