from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("胡航的界面")

def userlogin(request):
    return render(request,  "user.html")