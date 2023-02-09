from django.shortcuts import render

from . import util
from markdown2 import Markdown

def mdTohtml(title):
    contents = util.get_entry(title)
    markdowner = Markdown()
    if contents == None:
        return None
    else:
        return markdowner.convert(contents)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    html = mdTohtml(title)
    if html == None:
        return render(request, "encyclopedia/error.html", {
            "message": f"{title} does not exist in the entry."
        })
    else:
        return render(request, "encyclopedia/contents.html", {
            "contents": html,
            "title": title
        })

def search(request):
    if request.method == 'POST':
        title = request.POST['q']
        html = mdTohtml(title)
        if html == None:
            recommendations = []
            allEntries = util.list_entries()
            for entry in allEntries:
                if title.lower() in entry.lower():
                    recommendations.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommendations": recommendations
            })
        else:
            return render(request, "encyclopedia/contents.html", {
                "contents": html,
                "title": title
            })
    else:
        return httpRedirect("encyclopedia/index.html")


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['new']
        allEntries = util.list_entries()
        if title.lower() in allEntries():
            return render(request, "encyclopedia/error.html", {
                "message": f"{title} already exists."
            })
        else:
            util.save_entry(title, contents)
            return render(request, "encyclopedia)