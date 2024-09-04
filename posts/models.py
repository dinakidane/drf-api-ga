# posts/models.py
from django.db import models
from profiles.models import UserProfile

class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.author.user.username} on {self.created_at}'

