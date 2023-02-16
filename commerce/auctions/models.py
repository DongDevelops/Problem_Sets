from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Bids(models.Model):
    time = models.DateTimeField()
    amount = models.IntegerField()
    highest_bidder = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="highest_bidder")
    biddings = models.ManyToManyField(User, blank=True, related_name="biddings")

    def __str__(self):
        return f"{self.amount} at {self.time}"



class Listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    bid = models.ForeignKey(Bids, on_delete=models.CASCADE, related_name="bid")
    image = models.URLField(null=True, blank=True)
    watchlist = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="creator")
    listings = models.ManyToManyField(User, blank=True, related_name="listings")

    def __str__(self):
        return f"{self.id}: {self.title}"



class Comments(models.Model):
    comment = models.CharField(max_length=500)
    time = models.DateTimeField()
    commentor = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="commentor")
    item_comments = models.ManyToManyField(Listings, blank=True, related_name="item_comments")

    def __str__(self):
        return f"{self.comment} at {self.time}"