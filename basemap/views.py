
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout,models
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'login/homepage.html')
def loggingin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('basemap:index'))
        else:
            messages.warning(request,'Hatalı Giriş')
            return render(request,'login/login.html')
    else:
        return render(request,'login/login.html')
    return render(request,'login/login.html')
def register(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        email1= request.POST['email']
        password2=request.POST['repeat_password']
        if password2 == password1 and not User.objects.filter(username=username1).exists() and not User.objects.filter(email = email1).exists():
            user1=models.User.objects.create_user(username=username1,email=email1,password=password1)
            user1.save()
            user = authenticate(request, username=username1, password=password1)
            login(request,user)
            messages.success(request,'Başarıyla Kayıt Olundu')
            return HttpResponseRedirect(reverse('basemap:index'))
        elif password2 != password1 or User.objects.filter(username= username1).exists or User.objects.filter(email = email1).exists:
            messages.error(request,'Hata!,parolalarınız uyuşmuyor veya emailınız ve kullanıcı adınız halihazırda kullanılıyor')
            return render(request,'login/register.html')
        else:
            return render(request,'login/register.html')
    else:
        return render(request,'login/register.html')
    return render(request,'login/register.html')
@login_required(login_url='/login') 
def loggingout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basemap:index'))
@login_required(login_url='/login') 
def accountinfo(request):
    current_user=request.user
    if request.method=='POST':
        current_user.first_name=request.POST['first_name']
        current_user.last_name=request.POST['last_name']
        current_user.email=request.POST['email']
        current_user.save()
        return HttpResponseRedirect(reverse('basemap:account'))
    else:
        context={
            'current_user':current_user,
            'key':0,
        }
        return render(request,'login/account.html',context)

@login_required(login_url='/login')
def passwordchange(request):
    if request.method=='POST':
        changedpw=request.POST['changedpw1']
        if request.POST['changedpw1'] == request.POST['changedpw2'] and authenticate(username=request.user.username,password=changedpw)is None:
            messages.success(request,'Şifre Başarıyla Değiştirildi')
            request.user.make_password=request.POST['changedpw1']
            request.user.save()
            return HttpResponseRedirect(reverse('basemap:account'))
        else:
            messages.warning(request,("Lütfen şifrenizi eskisi ile aynı girmeyin ve şifrenizi doğrulayın."))
            return HttpResponseRedirect(reverse('basemap:account'))
    else:
        return HttpResponseRedirect(reverse('basemap:account'))

