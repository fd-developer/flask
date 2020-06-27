import random
import os

from PIL import Image, ImageFont, ImageDraw
import textwrap

from fbapp.models import Content, Gender

def find_content(gender):
	contents = Content.query.filter(Content.gender == Gender[gender]).all()
	return random.choice(contents)

class OpenGraphImage:

	def __init__(self, uid, first_name, description):
		background = self.base()
		self.location = self._location(uid)
		self.print_on_img(background, first_name.capitalize(), 70, 50)
		sentences = textwrap.wrap(description, width=60)

		current_h = 180

		self.print_on_img(background, description.capitalize(), 70, 100)
		#background.show()

		background.save(self._path(uid))

	def base(self):
		# Create a basic image
		img = Image.new('RGB', (1200, 630), '#18BC9C')
		return img

	def print_on_img(self, img, text, size, height):
		font = ImageFont.truetype(os.path.join('fbapp', 'static', 'fonts', 'Arcon-Regular.otf'), size)
		draw = ImageDraw.Draw(img)

		w, h = draw.textsize(text, font)

		position = ((img.width - w) / 2, height)

		draw.text(position, text, (255, 255, 255), font=font) 

		return w, h

	def _path(self, uid):
		return os.path.join('fbapp', 'static', 'tmp', '{}.jpg'.format(uid))
 
	def _location(self, uid):
		return 'tmp/{}.jpg'.format(uid)

# description = """You are beautifull"""

# OpenGraphImage(278653803499527, 'Fred', description)
