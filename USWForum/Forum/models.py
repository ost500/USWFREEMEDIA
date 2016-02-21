from __future__ import unicode_literals

from django.db import models

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
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    authors = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(default=0)
    
    
    def _unicode_(self):
        return self.title
    

    
# Create your models here.
