from django.db import models
import datetime
from swarms import Swarms


class Drones(models.Model):
    drone_id: int = models.IntegerField()
    drone_name: str = models.CharField(max_length=200)
    mac_address: str = models.CharField(max_length=200)
    ip_address: str = models.CharField(max_length=200)
    created_at: datetime = models.DateTimeField()
    updated_at: datetime = models.DateTimeField()
    swarm_id: int = models.ForeignKey(Swarms, on_delete=models.CASCADE)
    updated_by: int = models.IntegerField()
