from __future__ import unicode_literals

from django.db import models

# Create your models here.

class book(models.Model):
	"""class for books and attributes"""

	title_text = models.CharField(max_length=200)
	post_date = models.DateTimeField('date posted')
	def _unicode_(self):
		return unicode(self.title_text)
