from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40)
    sex = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    email = models.EmailField()
    def __unicode__(self):
        return self.last_name

class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    publisher = models.CharField(max_length=40)
    date = models.DateField()
    def __unicode__(self):
        return self.title
