from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    return HttpResponse("Hello there, hoping your alright.")

def aboutPage(request):
    return HttpResponse(" My name is KIWAGAMA HELLEN TUNWERE. I am a very adventourous lady, ready to grab every worth oppurtunity ,to explore alot of things. ")
