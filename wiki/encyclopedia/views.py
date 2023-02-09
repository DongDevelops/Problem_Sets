from django.shortcuts import render

from . import util
import markdown

def mdTohtml(title):
    content = util.get_entry(title)
    if content == None:
        return render("encyclopedia/error.html", {
            "message": "f{title} does not exist in the entry."
        })
    else:
        markdowner = markdown.Markdown()
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