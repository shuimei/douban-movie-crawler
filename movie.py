class DoubanMovie(object):
	"""docstring for DoubanMovie"""
	def __init__(self, items_dict):
		super(DoubanMovie, self).__init__()
		self.name = items_dict['name']
		self.director = items_dict['director']
		self.actors = items_dict['actors']
		self.release_date = items_dict['release_date']
		self.runtime = items_dict['runtime']
		self.douban_rating = items_dict['douban_rating']
		self.rating_people = items_dict['rating_people']
		self.genre = items_dict['genre']
		self.awards = items_dict['awards']
		self.post = items_dict['post']
		self.tages = items_dict['tages']

		