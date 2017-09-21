import urllib.request

class Image:
	
	def __init__(self, url, label):
		self.url = url
		self.label = label
		self.string_image = urllib.request.urlopen(url).read()

	def get_label(self):
		return self.label

	def get_url(self):
		return self.url

	def get_string_image(self):
		return self.string_image
