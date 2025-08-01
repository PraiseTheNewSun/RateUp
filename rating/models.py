from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(models.Model):
    post_caption = models.TextField()
    post_author = models.CharField(max_length=300, null=True)
    post_img = models.ImageField(upload_to='media/')
    post_date_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.post_caption

class Comment(models.Model):
    author = models.CharField(max_length=300, null=True)
    post_caption = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.author

class Detail(AbstractUser):
    # img = models.ImageField(upload_to='media/', null=True)
    pass

class ProfileImage(models.Model):
    image_user = models.CharField(max_length=300, null=True)
    img = models.ImageField(upload_to='media/profiles/', null=True)

    def __str__(self):
        return self.image_user
