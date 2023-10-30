from django.db import models
import datetime


class Swarms(models.Model):
    swarm_id: int = models.IntegerField(primary_key=True)
    swarm_name: str = models.CharField(max_length=200)
    created_at: datetime = models.DateTimeField()
    updated_by: int = models.IntegerField()
