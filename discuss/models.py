from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):

    name = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "帖子"
        verbose_name_plural = "帖子"
