from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Hello, world. You're at the important site index.")


def categories(request, important_number_id):
    if request.POST:
        print(f"POST: {request.POST}")

    if request.GET:
        print(f"GET: {request.GET}")

    if int(important_number_id) > 100:
        return redirect("home", permanent=True)

    return HttpResponse(f"<h1>Categories</h1><p>{important_number_id}</p>")


def archive(request, year):
    if int(year) > 2022:
        raise Http404()

    return HttpResponse(f"<h1>Archive by year </h1><p>{year}</p>")


def cat_details(request, cat_id):
    if int(cat_id) > 10:
        return redirect("home")  #temporary redirect 302

    return HttpResponse(f"<h1>Cats</h1><p>{cat_id}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>There is no truly exists page in this reality</h1>")

