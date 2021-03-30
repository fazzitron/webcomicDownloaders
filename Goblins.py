import urllib.request, urllib.error, urllib.parse, re

startURL = "https://www.goblinscomic.com/comic/06252005/"
nextRgx = "<a class=\"cc-next\" rel=\"next\" href=\"(https:\/\/www.goblinscomic.com\/comic\/[\\d\\w-]+)\">"
imageRgx = "src=\"(https:\/\/www.goblinscomic.com\/comics/.+jpg)\" id=\"cc-comic\""

baseURL = "https://www.giantitp.com/comics/"
linkRgx = """<IMG src="(https:\/\/i\.giantitp\.com\/\/comics\/oots\/.+)">"""

pageNum = 1

currentURL = str(startURL)

while (currentURL != None):
	print(currentURL)
	req = urllib.request.Request(currentURL, headers={'User-Agent' : "Magic Browser"})
	response = urllib.request.urlopen(req)
	webContent = response.read().decode('utf-8')
	
	imgMatch = re.findall(imageRgx, webContent)
	if (len(imgMatch) == 0):
		print("Can't find image at %s"%(currentURL))
		exit()
	for m in imgMatch:
		print(m)
		ext = m.split(".")[-1]
		fileName = "%i.%s"%(pageNum, ext)
		try:
			imgURL = m.replace(" ", "%20")
			imgReq = urllib.request.Request(imgURL, headers={'User-Agent' : "Magic Browser"})
			imgResponse = urllib.request.urlopen(imgReq)
			imgContent = imgResponse.read()
			
			imgFile = open(fileName, "wb")
			imgFile.write(imgContent)
			
			imgFile.close()
			
			print("%s written"%fileName)
		except:
			print("%s failed"%fileName)
	pageNum += 1
	
	nextMatch = re.findall(nextRgx, webContent)
	if (len(nextMatch) == 0):
		print("Can't find next at %s"%(currentURL))
		exit()
	for m in nextMatch:
		print(m)
		print("\n")
		currentURL = m
		

"""while (pageNum <= 1225):
	pageURL = baseURL + "oots%04i.html"%pageNum
	print(pageURL)
	req = urllib.request.Request(pageURL, headers={'User-Agent' : "Magic Browser"})
	response = urllib.request.urlopen(req)
	webContent = response.read().decode('utf-8')

	matches = re.findall(linkRgx, webContent)
	for m in matches:
		print(m)
		ext = m.split(".")[-1]
		fileName = "%i.%s"%(pageNum, ext)
		try:
			imgURL = m.replace(" ", "%20")
			imgReq = urllib.request.Request(imgURL, headers={'User-Agent' : "Magic Browser"})
			imgResponse = urllib.request.urlopen(imgReq)
			imgContent = imgResponse.read()
			
			imgFile = open(fileName, "wb")
			imgFile.write(imgContent)
			
			imgFile.close()
			
			print("%s written"%fileName)
		except:
			print("%s failed"%fileName)
	pageNum += 1
"""