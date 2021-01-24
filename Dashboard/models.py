# Create your models here.
from django.db import models

# Create your models here.
Statuses = ( 
    ("d", "Draft"), 
    ("p","Publish"),
   
) 





class Post(models.Model):
    
    
    Slug = models.SlugField(unique=True)
    MainText=models.TextField()
    Title = models.CharField(max_length=40,default='title')
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='app/static/img/post'  , null=True , default='app/static/img/post/default_news.jpeg')
    Status=models.CharField(max_length=20,choices=Statuses,default='p')
 


    class Meta:
        ordering = ['-date',]
    


    def __str__(self):
        return (self.Title)
