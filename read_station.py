from lxml import html
import requests

station_url = 'http://192.168.1.126/livedata.htm'

page = requests.get(station_url)
tree = html.fromstring(page.content)

out_temp = float(tree.xpath('//input[@name="outTemp"]')[0].value)
print ('Outdoor Temp: ', out_temp)
