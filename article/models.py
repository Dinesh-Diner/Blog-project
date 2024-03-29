from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=50)

    class Meta:
        verbose_name='Categorie'

    def __str__(self):
        return self.name

class  Article(models.Model):

    author=models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    category =models.ForeignKey(Category,on_delete = models.CASCADE,default='1')

    title=models.CharField(max_length=100)
    content=models.TextField(max_length=10000)
    img=models.ImageField(upload_to='article_images/',default='default_img.jpg')
    date=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.content}"
    def get_absolute_url(self):
        return reverse(":profile")
    
    
class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE ,related_name="comments")
    user=models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True) 
    text=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.created_date}: {self.text[:30]}"