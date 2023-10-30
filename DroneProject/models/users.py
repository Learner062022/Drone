from django.db import models


class Users(models.Model):
    user_id: int = models.IntegerField(primary_key=True)
    username: str = models.CharField(max_length=200)
    email: str = models.CharField(max_length=200)
