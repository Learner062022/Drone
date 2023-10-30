from django.db import models
import datetime


class Ap(models.Model):
    ap_id: int = models.IntegerField(primary_key=True)
    ssid: str = models.CharField(max_length=200)
    password: str = models.CharField(max_length=200)
    auth_method: str = models.CharField(max_length=200)
    created_at: datetime = models.DateTimeField()
    updated_at: datetime = models.DateTimeField()
    updated_by: int = models.IntegerField()
