from django.db import models
from accounts.models import User
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PostManager(models.Manager):
    
    def filter_by_post(self, user):
        return self.filter(user=user).all()


class Post(BaseModel):
    title = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    body = models.CharField(max_length=2200)
    picture = models.FileField(null=True, upload_to='post_picture/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    objects = PostManager()

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title


class Comment(BaseModel):
    body = models.TextField(max_length=2200)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'comments'

    
class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'likes'