# douban-movie-crawler
I have written a doouban movie crawler using python-requests and xpath syntax.
If you are intersted in data visualization, you can fetch this and have some analysis.

## settings.py
settings.py contains a dict which stores movie page numbers of year from 1880 to 2015 on douban site.
## DoubanMovieCrawler.py
DoubanMovieCrawler.py read `movie_pages` in settings.py and make requests to get movie name and its link, then write to a csv file named "%year%_douban_movies.csv".
## MovieRequests.py
this script reads file "douban_movie_by_year.csv" and make requests to fetch douban movie info. using xpath I find useful information.
a douban movie information I get from a movie item page contains:
+ subject: unique ID for every single movie
+ name: movie name
+ year: movie release year
+ directors: movie directors(one or more)
+ actors: starring actors
+ release_date: movie release date
+ star: douban movie rating
+ rating_peoplr: number of rating people
+ genres: movie types
+ awards: awards the movie have got
+ image_src: movie post
+ tags: common tags user defined
*note*: if any field was unavailable, it would be recorded as 'NotDefined'. 
