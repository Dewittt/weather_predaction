import requests
from pyquery import PyQuery as pq
from matplotlib import pyplot as plt
import re

partten = "\d.*?(\d+)℃"
x_labels = []
y_labels = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
    ,"Host":"tianqi.8684.cn"
}
html = requests.get("http://tianqi.8684.cn/hebei_qinhuangdao")
doc = str(html.content,"utf-8")
doc = pq(doc)
items = doc.find("body > div.weather > div.w-forecast.mb10 > div > ul:nth-child(2) li").items()
for item in items:
    x_labels.append(item.find("span").text())
    y_labels.append(int(str(re.findall(partten,item.find("p").text()))[2:-2]))
items = doc.find("body > div.weather > div.w-forecast.mb10 > div > ul.wf-mod.wf-mod7.wicon li").items()
for item in items:
    x_labels.append(item.find("span").text())
    y_labels.append(int(str(re.findall(partten, item.find("p").text()))[2:-2]))


plt.figure(figsize=(20,8),dpi=80)
plt.rcParams["font.sans-serif"] = ["simHei"]
plt.xticks(rotation = 45)
plt.grid(alpha=0.3)
plt.plot(x_labels,y_labels)
plt.show()
