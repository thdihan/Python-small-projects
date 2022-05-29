# -------------------
# Task: Web Scraper Using Standard Library
# -------------------
import urllib.request, urllib.error,urllib.parse
import re
import os
import sys

# Url Validity check 
def urlChecker (url) :
	try : 
		response = urllib.request.urlopen(url)
	except :
		response = 0
	return response

# Url & Folder name input (DEMO URL = "https://www.bdbooks.net/")
if (len(sys.argv) > 1) : # Using command line argument
	url = sys.argv[1]
else :
	print("Enter URL : ")
	url = input() # url input

response = urlChecker(url) # checking response for the first time

while (response == 0) : # loop for ignoring invalid url
	print("Invalid Input.\nEnter URL :")
	url = input()
	response = urlChecker(url) # checking url response again
	
if (len(sys.argv) == 3) : # Using command line argument
	foldername = sys.argv[2]
else :
	print("Enter Output Location/Folder : ")
	foldername = input() # folder name/location input

folderCheckCode = os.path.exists(foldername) # checking folder existance
if(folderCheckCode == False) :
	os.mkdir(foldername) # making folder

# Reading response html file and save it to index.html
webcontent = response.read(); 
open("index.html","wb").write(webcontent) # saving the html file to index.html

webcontent = str(webcontent) # converting it to string for easy to use

# Using Regular Expression <img> tag searching and downloading all image
pattern = '<img src="([^\s]+)"' # regex for link inside the img tag
matches = re.findall(pattern,webcontent) # getting all links

for imgUrl in matches :
	
	response = urlChecker(imgUrl) # checking image url
	if (response == 0) :
		continue
	image = response.read(); # reading image file

	filenamePattern = "[^\/]+$" # searching image actual name and extension from url
	filename = re.findall(filenamePattern,imgUrl) # getting image name with extension

	filename[0] = foldername+"/" + filename[0] # "foldername/imagename.extension"
	open(filename[0],"wb").write(image) # writing the image file

print("-- Downloaded Successfully --")