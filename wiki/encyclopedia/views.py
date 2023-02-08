from django.shortcuts import render

from . import util
from markdown2 import Markdown

def mdTohtml(md):
    markdowner = Markdown()
    html = markdowner.convert(md)
    return html

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def contents(request, title):
    html = mdTohtml(title.md)

    if title not in util.list_entries():
        return render(request, "encyclopedia/error.html", {
            "message": "f{title} does not exist in the entry."
        })
    else:
        return render(request, "encyclopedia/contents.html", {
        "contents": util.get_entry(),
        "title": title
        })