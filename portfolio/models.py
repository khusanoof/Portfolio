from django.db import models
from ckeditor.fields import RichTextField

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return f"{self.name}"
    
class Portfolio(models.Model):
    image = models.ImageField(upload_to='Images/portfolio')
    title = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    topic = models.CharField(max_length=100)
    description = RichTextField()
    def __str__(self):
        return f"{self.title}"



    
class Blog(models.Model):
    self_name = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    goal = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/blog')
    title = models.CharField(max_length=60)
    description = RichTextField()
    def __str__(self):
        return f"{self.title}"