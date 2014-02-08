import requests
import BeautifulSoup
import os

url = 'http://www.weather.com/weather/today/Austin+TX+78705:4:US'


def getTemperature():
	s = requests.session()
	soup = BeautifulSoup.BeautifulSoup(s.get(url).content)

	#GET TEMPERATURE
	temp = str(soup.find(itemprop="temperature-fahrenheit").string)
	

	inttemp = int(temp)
	temp = "It is " + temp + " degrees outside and "
	#GET WEATHER
	weather = str(soup.findAll('div', attrs={'class': 'wx-phrase '})[0].string) + ".  "
	temp = temp + weather
	

	if inttemp <= 32:
		temp = temp + "  It's pretty cold out there."
	elif inttemp <= 50:
		temp = temp + "  It's pretty chilly.  Wear a coat."
	elif inttemp <= 70:
		temp = temp + " It's alright, I suppose."
	elif inttemp <= 90:
		temp = temp + "  It's pretty hot out there."
	else:
		temp = temp + "  Jesus Christ it's way too hot out there."
	return temp

def sayIt(thing):
	os.system("espeak \""+thing+"\"")

if __name__ == "__main__":
	sayIt(getTemperature())