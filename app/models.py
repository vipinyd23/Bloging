from django.db import models
from django.contrib.auth.models import User,auth
from django.utils.html import format_html
from tinymce.models import HTMLField
class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style=:width:40px;height:40px;/>'.format(self.image))

class blogs(models.Model):
    blog_id=models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    date_posted=models.CharField(max_length=5)
    content=HTMLField()
    author=models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    # category= models.CharField(max_length=100)
    image=models.ImageField(upload_to='post/')

    def image_tag(self):
        return format_html('<img src="/media/{}" style=:width:50%;height:250px; />'.format(self.image))
    
 