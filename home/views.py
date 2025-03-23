from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    return HttpResponse("Hello there, hoping your alright. My name is KIWAGAMA HELLEN TUNWERE.")

def aboutPage(request):
    return HttpResponse("I am a very adventourous lady, ready to grab every worth oppurtunity ,to explore alot of things. ")
