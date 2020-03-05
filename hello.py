import json
import urllib
from urllib import urlopen


if __name__ == "__main__":
	url = urlopen("https://cve.circl.lu/api/last")
	data = url.read()
	result = json.loads(data)
	print '"Latest CVE is\n"', result[1]["summary"].format()


