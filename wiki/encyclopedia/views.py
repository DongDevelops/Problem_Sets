from django.shortcuts import render

from . import util
from markdown2 import Markdown

def mdTohtml(title):
    contents = util.get_entry(title)
    markdowner = Markdown()
    html = markdowner.convert(contents)
    return html

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):

    html = mdTohtml(title)

    if title not in util.list_entries():
        return render(request, "encyclopedia/error.html", {
            "message": "f{title} does not exist in the entry."
        })
    else:
        return render(request, "encyclopedia/contents.html", {
        "contents": html,
        "title": title
        })