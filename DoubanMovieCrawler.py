#-*—coding:utf8-*-
from lxml import etree
import requests
import re
import time
#编码转换
import sys
##reload(sys)
##sys.setdefaultencoding("utf-8")
from settings import movie_pages as mp
for k in mp.keys():
	year = k
	page_num = mp[k]
	print(year)
	print("-"*20)
	with open("%s_douban_movies.csv"%year,"a+") as f:
		for i in range(page_num + 1):
			start_url = "https://movie.douban.com/tag/%s?start=%d&type=T"%(year,i*20)
			#headers构造一个字典，里面保存了user-agent
			headers= { 'User-Agent' : 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36' }
			html = requests.get(start_url,headers=headers).content
			selector = etree.HTML(html)
			#xpath
			names = selector.xpath("//div[@class='pl2']/a/text()")
			img_name = selector.xpath("///a[@class='nbg']/img/@alt")
			links = selector.xpath("//div[@class='pl2']/a/@href")
			# rating = selector.xpath("//div[@class='pl2']/div/span[@class='rating_nums']/text()]")
			movie_dict = map(lambda a,c:(a,c), img_name, links)
			for m in movie_dict:
				# f.write("%s,%s\n"%(m[0],m[1]))
				try:
					f.write("%s,%s\n"%(m[0], m[1]))
				# print("%s,%s"%(m[0], m[2]))
				except UnicodeEncodeError:
					pass
			print(i*20)
			time.sleep(1)
	

