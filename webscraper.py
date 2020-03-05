from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'https://twitter.com/TheHackersNews'
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
print(url)
if __name__ == '__main__':

	tweets = soup.findAll("div", attrs={"class":"css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"})
	#print(content)
#	print(tweets)
#	tweet = content.find('div', attrs={"css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"}).text
	for x in tweets:
		print(x.text)

