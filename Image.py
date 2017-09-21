class Image:
	
	def __init__(self, url, label):
		self.url = url
		self.label = label

	def get_label(self):
		return self.label

	def get_url(self):
		return self.url

	def set_string__image(self, encoded_image):
		self.encoded_image = encoded_image

	def get_string_image(self):
		return self.encoded_image
