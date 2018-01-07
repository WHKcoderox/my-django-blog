from django.db import models
from django.utils import timezone

# Create your models here.

# Post model/table, with some fields and methods to push to db.
class Post(models.Model):
	""" Fields """
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = \
	models.DateTimeField(default=timezone.now)
	published_date = \
	models.DateTimeField(blank=True, null=True)

	""" methods """
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	""" str() method overload """
	def __str__(self):
		return self.title

