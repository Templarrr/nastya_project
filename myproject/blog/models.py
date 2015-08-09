from django.db import models
# from ckeditor.fields import RichTextField

BLOG_ITEM_STATUS = (
    ('0', 'Dratf'),
    ('1', 'Published'),
    ('2', 'Not Published'),
)

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	slug   = models.SlugField(unique=True)

#	def __str__(self):
#		return self.name


	def __unicode__(self):
		return self.name

class Post(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	slug   = models.SlugField(unique=True)
	body = models.TextField()
	#body = models.RichTextField()
	url = models.URLField()
	status = models.CharField(max_length=1, choices=BLOG_ITEM_STATUS, default='0')
	views = models.IntegerField(default=0)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

#	def __str__(self):
#		return self.title
	class Meta:
		ordering = ['created'] 

	def __unicode__(self):
		return self.title