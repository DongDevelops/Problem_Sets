from django.shortcuts import render

from . import util
from markdown2 import Markdown

def mdTohtml(title):
    contents = util.get_entry(title)
    if contents == None:
        return render("encyclopedia/error.html", {
            "message": "f{title} does not exist in the entry."
        })
    else:
        markdowner = Markdown()
        return markdowner.convert(contents)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    html = mdTohtml(title)
    return render(request, "encyclopedia/contents.html", {
        "contents": html,
        "title": title
    })