from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField()
    start_bid = models.IntegerField()

    pass

class Bids:
    pass

class Comments:
    pass