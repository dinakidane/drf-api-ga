# favourites/models.py
from django.db import models
from posts.models import Post
from profiles.models import UserProfile

class Favourite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.user.username} favoured {self.post}'
