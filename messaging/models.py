from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# this is a message model 
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10]

    def messages_between(self, user1, user2):
        return Message.objects.filter(
            (models.Q(sender=user1) & models.Q(receiver=user2)) |
            (models.Q(sender=user2) & models.Q(receiver=user1))
        ).order_by('-timestamp')
