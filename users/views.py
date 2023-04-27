from django.shortcuts import render
from django.http import HttpResponse


def landingPage(request):
    context = {}
    return render(request, "users/landing_page.html", context)
