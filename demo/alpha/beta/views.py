from django.shortcuts import render
from.models import std
from django.http import HttpResponse
# Create your views here.
def display(re):
    return HttpResponse('hello')