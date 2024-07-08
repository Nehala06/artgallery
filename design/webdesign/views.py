from django.shortcuts import render,redirect
from django.http import HttpResponse
from webdesign.models import registration


def hello (request):
    return HttpResponse("Welcome to my Official Website Art Gallery")

def itemp(request):
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')

def signup(request):
    if request.method =="POST":
        sign = registration(email=request.POST.get("email"),
                   password=request.POST.get("psw"),
                   passwordre=request.POST.get("pswr"))
        sign.save()
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        users = registration.objects.filter(email=uname)
        if users.exists():
            for user in users:
                if pwd == user.password:
                    request.session['sid'] = user.email
                    return render(request, 'booking.html')
            return HttpResponse("INCORRECT PASSWORD")
        else:
            return HttpResponse("USERNAME DOESN'T EXCIST")

    return render(request, 'login.html')
