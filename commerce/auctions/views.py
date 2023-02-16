from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import User, Comments, Bids, Listings


def index(request):
    active_listings = Listings.objects.filter(active=True)
    return render(request, "auctions/index.html", {
            "listings": active_listings
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
        new_listing.listings.add(user)
        new_listing.save()

        return render(request, "auctions/index.html", {
            "listings": Listings.objects.all()
        })

    else:
        return render(request, "auctions/create.html")


def item(request, listing_id):
        listing = Listings.objects.get(id=listing_id)
        listing.
        username = request.POST["username"]
        creator = request.POST["creator"]
        comments = listing.item_comments.all()

        close = listing
        watchlist = listing
        if username != creator and listing.watchlist == False:
            return render(request, "auctions/item.html", {
                "watchlist": watchlist,
                "comments": comments
            })
        elif username != creator and listing.watchlist == True:
                return render(request, "auctions/item.html", {
                    "comments": comments
                })
        elif username == creator and listing.watchlist == False:
                return render(request, "auctions/item.html", {
                    "watchlist": watchlist,
                    "close": close,
                    "comments": comments
                })
        elif username == creator and listing.watchlist == False:
                return render(request, "auctions/item.html", {
                    "close": close,
                    "comments": comments
                })


@login_required
def place_bid(request):
    if request.method == "POST":
        new_bid = int(request.POST["place_bid"])
        original_bid = int(request.POST["amount"])
        id = request.POST["id"]
        username = request.POST["username"]
        user = User.objects.get(username=username)
        now = datetime.now()
        if new_bid > original_bid:
            New = Bids(time=now, amount=new_bid, highest_bidder=user)
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
    if request.method == "POST":
        item_id = request.POST["id"]
        item = Listings.objects.get(id=item_id)
        item.active = False
        item.save()
        winner = item.bid.highest_bidder

        return render(request, "auctions/item.html", {
            "message": f"This listing is closed, the winner is {winner}."
        })
    else:
        return render(request, "auctions/index.html")


def closed(request):
    closed_listings = Listings.objects.filter(active=False)
    return render(request, "auctions/closed.html", {
            "listings": closed_listings
        })

def closed_item(request, id):
    if request.method == "POST":
        id = request.POST["id"]
        item = Listings.objects.get(id=id)
        winner = item.bid.highest_bidder
        title = request.POST["title"]
        description = request.POST["description"]
        amount = request.POST["amount"]
        time = request.POST["time"]
        image = request.POST["image"]
        return render(request, "auctions/closed_item.html", {
                "id": id,
                "title": title,
                "description": description,
                "amount": amount,
                "time": time,
                "image": image,
                "message": f"This listing is closed, the winner is {winner}."
        })
    else:
        return render(request, "auctions/index.html")

@login_required
def comments(request, listing_id):
    if request.method == "POST":
        listing = Listings.objects.get(id=listing_id)
        comment = request.POST["comment"]
        current_time = datetime.now()
        username = request.POST["username"]
        user = User.objects.get(username=username)
        new_comment = Comments.objects.create(time=current_time, commentor=user, comment=comment)
        new_comment.item_comments.add(listing)

        return HttpResponseRedirect(reverse("item", args=(listing.id,)))