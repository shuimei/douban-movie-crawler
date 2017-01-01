import requests
from lxml import etree
from functools import reduce
import os
import time
def readMovieUrl(fileObject):
		try:
			line = fileObject.__next__().rstrip("\n").split(",")
			name, url = line[0], line[-1]
			# print("%s,%s"%(name, url))
			return name, url
		except StopIteration:
			print("StopIteration:You have read the end of the file.")
			return False

def getMovieInfo(name, url):
	headers= { 	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
				"Accept-Encoding":"gzip, deflate, sdch, br",
				"Accept-Language":"zh-CN,zh;q=0.8",
				"Connection":"keep-alive",
				"Cookie":"""bid=kpxCiW7R8hs; gr_user_id=8f0e789b-73f6-4cb1-9a24-5b869a75a210; _vis_opt_s=1%7C; _vwo_uuid=2AFCCB8D3179301BA1F82CBA5E5C3019; _vis_opt_exp_32_combi=1; _vis_opt_exp_31_combi=1; _vis_opt_exp_31_goal_1=1; nlsrid228272=2; enable_push_desktop_noty=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1483159666%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; ll="108296"; ps=y; ue="betasdeng1992@sina.cn"; dbcl2="61295987:Gj+YkB6qPjU"; ck=rOkM; _vwo_uuid_v2=C950AFE94CFE50C746119810AF4030E2|c2a5cd204eef39355588d689285bfb0d; ap=1; __utmt=1; push_noty_num=0; push_doumail_num=0; __utmt_douban=1; __utma=30149280.160500193.1479529210.1483030234.1483159666.19; __utmb=30149280.17.10.1483159666; __utmc=30149280; __utmz=30149280.1482247417.13.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.6129; __utma=223695111.1509095869.1479529229.1483030234.1483159666.17; __utmb=223695111.0.10.1483159666; __utmc=223695111; __utmz=223695111.1482236291.9.9.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=ce737c7a0a3f1960.1479529230.17.1483162912.1483032917.; _pk_ses.100001.4cf6=*""",
				"DNT":"1",
				"Host":"movie.douban.com",
				"Upgrade-Insecure-Requests":"1",
				"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
				}
	html = requests.get(url,headers=headers).content.decode("utf-8")
	selector = etree.HTML(html)
	strCat = lambda x,y:x+"/"+y
	# movie subject
	subject = url.split("/")[-2]
	# movie name
	tmp = selector.xpath("//h1/span[@property='v:itemreviewed']/text()")
	name = len(tmp) == 0 and "NotDefined" or reduce(strCat, tmp)
	# movie release year
	tmp = selector.xpath("//h1/span[@class='year']/text()")
	year = len(tmp) == 0 and "NotDefined" or reduce(strCat, tmp)
	# movie director(s)
	tmp = selector.xpath("//a[@rel='v:directedBy']/text()")
	directors = len(tmp) == 0 and "NotDefined" or reduce(strCat, tmp)
	# movie actor(s)
	tmp = selector.xpath("//a[@rel='v:starring']/text()")
	actors = len(tmp) == 0 and "NotDefined" or reduce(strCat, tmp)
	# movie release date
	tmp = selector.xpath("//span[@property='v:initialReleaseDate']/text()")
	date = len(tmp) == 0 and "NotDefined" or reduce(strCat, tmp)
	# movie runtime
	tmp = selector.xpath("//span[@property='v:runtime']/text()")
	time = len(tmp) == 0 and "NotDefined" or reduce(strCat, tmp)
	# movie rating by douban site
	tmp = selector.xpath("//strong[@class='ll rating_num']/text()")
	star = len(tmp) == 0 and "NotDefined" or reduce(strCat, tmp)
	# number of rating people
	tmp = selector.xpath("//span[@property='v:votes']/text()")
	rating_people = len(tmp) == 0 and "NotDefined" or reduce(strCat, tmp)
	# movie genre
	tmp = selector.xpath("//span[@property='v:genre']/text()")
	genres = len(tmp) == 0 and "NotDefined" or reduce(strCat, tmp)
	# movie award
	tmp = selector.xpath("//ul[@class='award']/li/text() | //ul[@class='award']/li/a/text()")
	awards = len(tmp) == 0 and "NotDefined" or reduce(strCat, tmp).replace("\n","")
	awards = awards.replace(" ","")
	# str_awards = reduce(strCat, awards)
	# movie post image url
	tmp = selector.xpath("//a[@class='nbgnbg']/img[@rel='v:image']/@src")
	image_src = len(tmp) == 0 and "NotDefined" or reduce(strCat, tmp)
	# # movie introduction
	# tmp = selector.xpath("//span[@property='v:summary']/text()")
	# introduction =  len(tmp) == 0 and "NotDefined" or tmp[0]
	# str_introduction = reduce(strCat, introduction)
	# movie common tags
	tmp = selector.xpath("//div[@class='tags-body']/a/text()")
	tags = len(tmp) == 0 and "NotDefined" or reduce(strCat, tmp)
	# summary
	movie_info = {
		"subject":subject,
		"name": name,
		"year": year,
		"directors": directors,
		"actors": actors,
		"release_date": date,
		"runtime": time,
		"star": star,
		"rating_people": rating_people,
		"genres": genres,
		"awards": awards,
		"image_src": image_src,
		# "introduction": str_introduction,
		"tags": tags,
	}
	return movie_info



if __name__ == '__main__':
	strCat = lambda x,y:x+","+y
	output = open("douban_movie_info_by_year.csv", "a+", encoding='utf-8')
	with open("douban_movie_by_year.csv","r") as f:
		count = 0
		while True:
			count = count + 1
			if count % 100 == 0:
				print(count)
			name, url = readMovieUrl(f)
			dm = getMovieInfo(name, url)
			for k in dm.keys():
				dm[k] = dm[k].replace(",","-")
			infos = [
				dm["subject"], dm["name"], dm["year"], dm["directors"], dm["actors"],
				dm["release_date"], dm["runtime"], dm["star"], dm["rating_people"],dm["genres"],
				dm["awards"], dm["tags"], dm["image_src"]
			]
			print(infos)
			output.write(reduce(strCat, infos))
			output.write("\n")
			time.sleep(0.1)


			


	# dm = getMovieInfo("悠闲的行人，敞篷巴士与拉着马车小跑的马匹 Leisurely Pedestrians, Open Topped Buses and Hansom Cabs with Trotting Horses","https://movie.douban.com/subject/2148860/")
	# for k in dm.keys():
	# 	dm[k] = dm[k].replace(",","-")
	# 	print(k,dm[k])
	


