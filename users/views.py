from django.shortcuts import render
from django.http import HttpResponse






def landingPage(request):
    return HttpResponse(f"Hello, Welcome to the landing page")














