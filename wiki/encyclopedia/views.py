from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def contents(request):
    title = request.get.title
    if title not in util.list_entries():
        return render(request, "encyclopedia/error.html", {
            "message": "${title} does not exist in the entry."
        })
    else:
        return render(request, "encyclopedia/contents.html", {
        "contents": util.get_entry()
        })