from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("<b>Konbanwa it241!</b>")