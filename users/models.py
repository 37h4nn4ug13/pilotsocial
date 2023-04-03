from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# friend model  
class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    # cls is the class itself and is not self because we are not creating an instance of the class
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

    @classmethod
    def get_friends(cls, current_user):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        return friend.users.all()

    def __str__(self):
        return self.current_user.username