from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)
    
class Blog(models.Model):
    blogTitle = models.CharField(max_length=100)
    blogDescription = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    
