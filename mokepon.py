import urllib.request, urllib.error, urllib.parse, re

baseURL = "https://h0lyhandgrenade.co.uk/mokepon/comic/"
baseDownload = "https://h0lyhandgrenade.co.uk"
linkRgx = """<meta property="og:image" content="(\/mokepon\/assets\/images\/comics\/\d+\/.+\.[ejnp]+g)"\/>"""

pageNum = 1

while (pageNum <= 1032):
	pageURL = baseURL + str(pageNum)
	response = urllib.request.urlopen(pageURL)
	webContent = response.read().decode('utf-8')

	matches = re.findall(linkRgx, webContent)
	for m in matches:
		fileName = "%i.png"%(pageNum)
		fileName = "0"*(8-len(fileName)) + fileName
		try:
			imgURL = (baseDownload + m).replace(" ", "%20")
			imgResponse = urllib.request.urlopen(imgURL)
			imgContent = imgResponse.read()
			
			imgFile = open(fileName, "wb")
			imgFile.write(imgContent)
			
			imgFile.close()
			
			print("%s written"%fileName)
		except:
			print("%s failed"%fileName)
	pageNum += 1
