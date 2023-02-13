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

        amount = request.POST["starting_bid"]
        now = datetime.now()
        bid = Bids(time=now, amount=amount)
        bid.save()

        new_listing = Listings(title=title, image=image, description=description, bid=bid)
        new_listing.save()

        return render(request, "auctions/index.html", {
            "listings": Listings.objects.all()
        })

    else:
        return render(request, "auctions/create.html")


def item(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        amount = request.POST["amount"]
        time = request.POST["time"]
        image = request.POST["image"]
        return render(request, "auctions/item.html", {
            "title": title,
            "description": description,
            "amount": amount,
            "time": time,
            "image": image
        })

    else:
        return render(request, "auctions/index.html")

def place_bid(request):
    if request.method == "POST":
        