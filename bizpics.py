from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import requests
import urllib.request
import binascii
import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
from webcolors import hex_to_name

colorlist = []
a = 1


def imagecalc():
	NUM_CLUSTERS = 5
	print('reading image')
	im = Image.open('img/image.jpg')
	im = im.resize((150, 150))  # optional, to reduce time
	ar = np.asarray(im)
	shape = ar.shape
	ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

	codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

	vecs, dist = scipy.cluster.vq.vq(ar, codes)  # assign codes
	counts, bins = scipy.histogram(vecs, len(codes))  # count occurrences

	index_max = scipy.argmax(counts)  # find most frequent
	peak = codes[index_max]
	colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
	colourRGB = convertToRGB(colour)
	colorlist.append(colourRGB)

def convertToRGB(hexColor):
        h = hexColor
        rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        return(rgb)



count = 0
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://4chan.org/biz/catalog")
images = driver.find_elements_by_tag_name('img')

for image in images:
	urllib.request.urlretrieve(image.get_attribute('src'), 'img/image' + '.jpg')
	try:
		imagecalc()
	except:
		print("oof")
	count += 1

driver.close()

print(colorlist)

redTotal = 0
greenTotal = 0
imageTotal = 0

for rgbValue in colorlist:
	green = rgbValue[0]
	red = rgbValue[1]
	greenTotal += green
	redTotal += red
	imageTotal += 1
	
greenAvg = greenTotal / imageTotal
redAvg = redTotal / imageTotal
##TODO check for what makes an image green lol 

print(greenAvg)
print(redAvg)
print(imageTotal)
