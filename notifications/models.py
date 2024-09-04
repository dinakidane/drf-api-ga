# notifications/models.py
from django.db import models
from profiles.models import UserProfile
from posts.models import Post

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('COMMENT', 'Comment'),
        ('FOLLOW', 'Follow'),
        ('FAVOURITE', 'Favourite'),
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user.user.username} - {self.notification_type}'

