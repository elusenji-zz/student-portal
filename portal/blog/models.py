from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 100, unique = True, db_index = True)
	slug = models.SlugField(max_length = 100, unique = True)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	category = models.ForeignKey('blog.Category')

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		#return ('post_detail', None, {'slug': self.slug})
		#return reverse('post_detail', None, {'slug': self.slug})
		return reverse('post_detail', args=[self.slug])

class Category(models.Model):
	title = models.CharField(max_length = 100, db_index = True)
	slug = models.SlugField(max_length = 100, db_index = True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return HttpResponseRedirect(reverse('post_list', None, {'slug': self.slug}))
