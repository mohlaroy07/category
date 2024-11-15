from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=244)
    
    def __str__(self) -> str:
        return self.name
    
    
class Article(models.Model):
    title = models.CharField(max_length=244)
    content = models.TextField()
    published_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    author = models.CharField(max_length=244)
    
    def __str__(self) -> str:
        return self.title - self.content
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=244)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.user - self.text
        