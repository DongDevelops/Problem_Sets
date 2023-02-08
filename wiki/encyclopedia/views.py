from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def contents(request):
    return render(request, "encyclopedia/contents.html", {
        "contents": util.get_entry()
    })