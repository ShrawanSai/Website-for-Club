from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200,blank = True)
    author = models.CharField(max_length=200)
    description = RichTextField(blank = True, null = True)
    date = models.DateField()
    blog_image = models.ImageField(upload_to='board/images/',blank = True)

    def __str__(self):
        return self.title
