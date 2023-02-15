from django.contrib.auth.models import AbstractUser
from django.db import models

class Bids(models.Model):
    time = models.DateTimeField()
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.amount} at {self.time}"

class Listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    bid = models.ForeignKey(Bids, on_delete=models.CASCADE, related_name="bid")
    image = models.URLField(null=True, blank=True)
    watchlist = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}: {self.title}"

class User(AbstractUser):
    listing = models.ManyToManyField(Listings, blank=True, related_name="listing")
    pass

class Comments(models.Model):
    comments = models.CharField(max_length=500)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.comments} at {self.time}"