import urllib.request, urllib.error, urllib.parse, re

baseURL = "https://www.giantitp.com/comics/"
linkRgx = """<IMG src="(https:\/\/i\.giantitp\.com\/\/comics\/oots\/.+)">"""

pageNum = 1179

while (pageNum <= 1201):
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
