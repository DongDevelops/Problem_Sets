from django.contrib import admin
from .models import Listings, Bids, User, Comments, Categories
# Register your models here.

admin.site.register(Listings)
admin.site.register(Comments)
admin.site.register(Bids)
admin.site.register(User)
admin.site.register(Categories)
