from django.shortcuts import render

from . import util
from markdown2 import Markdown

def mdTohtml(title):
    if title is in util.list_entries():
        contents = util.get_entry(title)
        markdowner = Markdown()
        return markdowner.convert(contents)
    else:
        return render("encyclopedia/error.html", {
            "message": "f{title} does not exist in the entry."
        })

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    html = mdTohtml(title)
    if html == None:
        return render(request, "encyclopedia/error.html", {
            "message": "f{title} does not exist in the entry."
        })
    else:
        return render(request, "encyclopedia/contents.html", {
        "contents": html,
        "title": title
        })