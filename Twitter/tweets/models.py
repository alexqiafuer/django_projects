from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField(null=True, blank=True)
    images = models.FileField(upload_to='images/', blank=True)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            'id': self.id, 
            'content':self.content, 
            'likes': 17
        }