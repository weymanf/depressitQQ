from django.db import models

class Post(models.Model):
  body = models.CharField(max_length=1500)
  votes = models.IntegerField(default=0)
  pub_date = models.DateTimeField('date published')
  
  
class Comment(models.Model):
  body = models.CharField(max_length=1500)
  votes = models.IntegerField(default=0)
  pub_date = models.DateTimeField('date published')
  post = models.ForeignKey(Post)
  
  
# How the fuckkkkk
# class User(models.Model):
#   user_name = models.CharField(max_length=13)
