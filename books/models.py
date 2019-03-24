from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 200)
	Author = models.CharField(max_length = 150)
	description = models.TextField()
	condn = models.TextField(blank=True)
	timestamp = models.DateTimeField(auto_now_add = True)
	cover = models.ImageField(upload_to = 'gallery',blank=True)
	email = models.CharField(max_length = 100, blank=True)

	def __str__(self):
		return f"{self.id}.{self.title}"


		