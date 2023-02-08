from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def contents(request):
    if not in util.list_entries():
        return render(request, "encyclopedia/error.html", {
            "message": Entry doesn't exist.
        })
    else:
        return render(request, "encyclopedia/contents.html", {
        "contents": util.get_entry()
    })