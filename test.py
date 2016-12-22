#-*—coding:utf8-*-
from lxml import etree
import requests
import re
#编码转换
import sys
##reload(sys)
##sys.setdefaultencoding("utf-8")
start_url = "https://movie.douban.com/subject/26720220/"
#headers构造一个字典，里面保存了user-agent
headers= { 'User-Agent' : 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36' }
html = requests.get(start_url,headers=headers).content
selector = etree.HTML(html)

#xpath
name = selector.xpath("//h1/span[@property='v:itemreviewed']/text()")[0]
# director = selector.xpath("//a[@rel='v:directedBy']/text()")[0]
year = selector.xpath("//h1/span[@class='year']/text()")[0]
rating = selector.xpath("//strong[@class='ll rating_num']/text()")
actors = selector.xpath("//a[@rel='v:starring']/text()")
##info = selector.xpath("//div[@id='info'/text()]")
f=open("tmp.txt","a+")
f.write("%s,%s"%(name,year))
