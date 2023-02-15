from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import User, Comments, Bids, Listings


def index(request):
    return render(request, "auctions/index.html", {
            "listings": Listings.objects.all()
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        image = request.POST["image"]
        username = request.POST["username"]
        user = User.objects.get(username=username)
        amount = request.POST["starting_bid"]
        now = datetime.now()
        bid = Bids(time=now, amount=amount)
        bid.save()
        new_listing = Listings(title=title, creator=user, image=image, description=description, bid=bid)
        new_listing.save()

        return render(request, "auctions/index.html", {
            "listings": Listings.objects.all()
        })

    else:
        return render(request, "auctions/create.html")


def item(request, id):
    if request.method == "POST":
        id = request.POST["id"]
        title = request.POST["title"]
        description = request.POST["description"]
        amount = request.POST["amount"]
        time = request.POST["time"]
        image = request.POST["image"]
        username = request.POST["username"]
        creator = request.POST["creator"]
        update = Listings.objects.get(id=id)
        if username == creator:
            close = Y
        if update.watchlist == False:
            watchlist = Y
            return render(request, "auctions/item.html", {
                "id": id,
                "title": title,
                "description": description,
                "amount": amount,
                "time": time,
                "image": image,
                "watchlist": watchlist
            })
        else:
            return render(request, "auctions/item.html", {
                "id": id,
                "title": title,
                "description": description,
                "amount": amount,
                "time": time,
                "image": image,
            })
    else:
        return render(request, "auctions/index.html")


@login_required
def place_bid(request):
    if request.method == "POST":
        new_bid = int(request.POST["place_bid"])
        original_bid = int(request.POST["amount"])
        id = request.POST["id"]
        now = datetime.now()
        if new_bid > original_bid:
            New = Bids(time=now, amount=new_bid)
            New.save()
            Update = Listings.objects.get(id=id)
            Update.bid = New
            Update.save()

            return render(request, "auctions/message.html", {
                "message": "Succeffully bidded."
            })
        else:
            return render(request, "auctions/message.html", {
                "message": f"New bid should be greater than original bid({original_bid})."
            })

    else:
        return render(request, "auctions/index.html")


@login_required
def watchlist(request):
    if request.method == "POST":
        id = request.POST["id"]
        item = Listings.objects.get(id=id)
        item.watchlist = True
        item.save()
        watchlist_items = Listings.objects.filter(watchlist=True)
        return render(request, "auctions/watchlist.html", {
            "items": watchlist_items
        })
    else:
        watchlist_items = Listings.objects.filter(watchlist=True)
        return render(request, "auctions/watchlist.html", {
            "items": watchlist_items
        })


@login_required
def remove(request):
    if request.method == "POST":
        id = request.POST["id"]
        item = Listings.objects.get(id=id)
        item.watchlist = False
        item.save()
        watchlist_items = Listings.objects.filter(watchlist=True)
        return render(request, "auctions/watchlist.html", {
            "items": watchlist_items
        })
    else:
        watchlist_items = Listings.objects.filter(watchlist=True)
        return render(request, "auctions/watchlist.html", {
            "items": watchlist_items
        })


@login_required
def close(request):

    pass