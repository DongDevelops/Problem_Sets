from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("item/<int:id>", views.item, name="item"),
    path("place_bid", views.place_bid, name="place_bid"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("remove", views.remove, name="remove"),
    path("close", views.close, name="close"),
    path("closed", views.closed, name="closed")
]
