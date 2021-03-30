from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    title = "Welcome page"
    # doc = "<h1>{title}</h1>".format(title = title)
    # django_redered_doc = "<h1>{{title}}</h1>".format(title = title)
    return render(request, "hello_world.html", {"title": title})


def contact_page(request):
    title = "Contact page"
    return HttpResponse("<h1> Contact Us</h1>")
