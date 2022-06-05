import django
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from fileshare.models import FileUploadModel, TextReflectorModel
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
from .forms import FileForm

@login_required
def indexview(request):
    files = FileUploadModel.objects.all()
    print(request.user_agent.os)
    return render(request, "fileshare/allfiles.html",{
        "files":files
    })

@login_required
def uploadfileview(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    form = FileForm()
    return render(request, "fileshare/uploadfile.html",{
        "form":form
    })

def successview(request):
    return render(request, "fileshare/success.html")


class delefile(APIView):
    def post(self, request):
        try:
            f = request.data["fid"]
            a = FileUploadModel.objects.get(f_id = f)
            a.delete()
            return Response({"resp":"success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"resp":"fail"})             

@login_required
def textreflectorview(request):
    # data = TextReflectorModel.objects.all().first().text
    try:
        data = TextReflectorModel.objects.get(user=request.user).text
    except:
        a = TextReflectorModel.objects.create(user=request.user, text="Enter text here")
        a.save()

    data = TextReflectorModel.objects.get(user=request.user).text

    return render(request, "fileshare/t2.html",{
        "data":data
    })

class textreflectorapi(APIView):
    def post(self, request):
        t = request.data["text"]
        a = TextReflectorModel.objects.get(user=request.user)
        a.text = t
        a.save()
        return Response({"resp":"success"}, status=status.HTTP_200_OK)


def loginview(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "fileshare/login.html", {
                "message": "Invalid username or password."
        })
    
    else:
        if request.user.is_authenticated:
            
            return HttpResponseRedirect(reverse("index"))
        return render(request,"fileshare/login.html")
 

def registerview(request):
    if request.method == "POST":
        username = request.POST["username"]
        # email = request.POST["email"]
        # username = username.replace(" ", "")
        # print(username)
        # return HttpResponseRedirect(reverse("indexguest"))
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        email = ""
        if password != confirmation:
            return render(request, "fileshare/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "fileshare/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        a = TextReflectorModel.objects.create(user=user, text="Enter text here")
        a.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        if request.user.is_authenticated:
            
            return HttpResponseRedirect(reverse("index"))
        return render(request, "fileshare/register.html")

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginview'))

class checkusername(APIView):
    def post(self,request):
        username = request.data["username"]
        if User.objects.filter(username = username).exists():
            return Response({"resp":"not-available"}, status=status.HTTP_226_IM_USED)
        else:
            return Response({"resp":"available"}, status=status.HTTP_200_OK)

def urlqrview(request):
    return render(request, "fileshare/urlqr.html")


def tempfun(request):
    return render(request, "fileshare/video.html")