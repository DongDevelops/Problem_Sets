from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField()
    start_bid = models.IntegerField(min_value=10)

    def __str__(self):
        return f"{self.id}: {self.title}"

class Bids:
    pass

class Comments:
    pass