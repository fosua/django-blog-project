from django.db import models
from django.contrib import admin

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=60)
	body = models.TextField()
	date_created = models.DateField(auto_now_add= True)
	date_updated = models.DateField(auto_now = True)
	def __unicode__(self):
		return self.title
class Comment(models.Model):
	body = models.TextField()
	author = models.CharField(max_length= 60)
	date_created = models.DateField(auto_now_add= True)
	date_updated = models.DateField(auto_now= True)
	post_comment = models.ForeignKey(Post)
	def __unicode__(self):
		return self.author
	def first_sixty_body(self):
		return self.body[:60]
#create modelAdmin classes
class CommentAdmin(admin.ModelAdmin):
	list_display = ('post_comment','author','first_sixty_body','date_created', 'date_updated')
	list_filter = ('date_created', 'author')
class CommentInline(admin.TabularInline):
	model = Comment
class PostAdmin (admin.ModelAdmin):
	list_display =('title', 'date_created','date_updated')
	search_fields = ('title', 'body')
	list_filter = ('date_created',)
	inlines = [CommentInline]
	
	
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

