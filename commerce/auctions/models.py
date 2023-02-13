from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField()
    bid = models.ForeignKey(Bids, on_delete=models.CASCADE, related_name="bid")

    def __str__(self):
        return f"{self.id}: {self.title}"

class Bids(models.Model):
    time = models.DateTimeField()
    amount = models.IntegerField(min_value=10)

    def __str__(self):
        return f"{self.amount} at {self.time}"

class Comments(models.Model):
    comments = models.CharField()
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.comments} at {self.time}"