from __future__ import unicode_literals

from django.db import models
from pip._vendor.ipaddress import ip_address

# class Publisher(models.Model):
#     name = models.CharField(max_length=50)
#     def _unicode_(self):
#         return self.name
#     
# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     def _unicode_(self):
#         return self.name
# 
# class Article(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.CharField(max_length=100)
#     authors = models.ForeignKey(Author,blank=True, null=True)
#     publisher = models.ForeignKey(Publisher,blank=True, null=True)
#     publication_date = models.DateField(blank=True, null=True)
#     
#     def _unicode_(self):
#         return self.title

class Category(models.Model):
    category = models.CharField(max_length=100, default='')
    
    def _unicode_(self):
        return self.id
      
class Media(models.Model):
    picture = models.FilePathField(null=True)
    video = models.FilePathField(null=True)
    A_id = models.IntegerField(default=0)
    
    def _unicode_(self):
        return self.picture
    
class Article(models.Model):
    category = models.ForeignKey(Category,null=True, blank=True, default='')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    authors = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(default=0)
    IP_addr = models.GenericIPAddressField(default = '')
    media = models.ForeignKey(Media,blank=True,null=True)
    
    def _unicode_(self):
        return u'%s %s %s' % (self.id, self.title, self.content)
    

    
# Create your models here.
