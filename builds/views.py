
from django.http import HttpResponse, HttpResponseRedirect
from .models import Buildorders,voters,comments
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login,models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def index(request):
    recent_4_age=[]
    for a in ('Dark Age','Feudal Age','Castle Age','Imperial Age','Post Imperial Age','Dark_Age','Feudal_Age','Castle_Age','Imperial_Age','Post_Imperial_Age'):
            b=Buildorders.objects.filter(age=a).order_by('-pub_date')[:4]
            recent_4_age.append(b)
    top_10=Buildorders.objects.order_by('-vote')[0:10]
    latest_order_list = Buildorders.objects.order_by('-pub_date')[:5]
    context = {
        'latest_order_list': latest_order_list,
        'recent_4_age':recent_4_age,
        'top_10':top_10,
    }
    return render(request, 'builds/index.html', context)
def detail(request,build_id):
    if Buildorders.objects.filter(pk=build_id).exists():
        if Buildorders.objects.filter(pk=build_id)[0].approved:
            build_list_raw=Buildorders.objects.filter(pk=build_id)[0].build_list
            build_list_raw.split("&",)
            build_list=[]
            for i in build_list_raw.split("&",):
                if i=='&' or i=="":
                   continue
                else :
                    build_list.append(i)
            if request.method=='POST':
                current=Buildorders.objects.filter(pk=build_id).first()
                add_comment=comments(comuser_id=request.user.id,comtext=request.POST['comment'],comid=current)
                add_comment.save()
                return redirect('builds:detail',build_id=build_id)
            else:
                key=0
                comments1=comments.objects.filter(comid=build_id,approved=True)
                build = get_object_or_404(Buildorders, pk=build_id)
                if request.user.is_authenticated:
                    key=2
                    if build.username_id ==request.user.id:
                        key=1
            return render(request,'builds/builddetail.html',{'build':build,'key':key,'comments':comments1,'build_list':build_list})
        else:
            messages.error(request,'Böyle Bir Buildorder Yok')
            return redirect('builds:index')
    else:
        messages.error(request,'Böyle Bir Buildorder Yok')
        return redirect('builds:index')
def results(request,build_id):
    return HttpResponse("selamresult%s"%build_id)
@login_required(login_url='/login')
def add(request):
    user=request.user.username
    if request.method=='POST':
        build_list=""
        for i in range(1,18):
            if request.POST['list%s' %i]:
                listitem=request.POST['list%s' %i]
                build_list+=str(listitem)+"&"
            else:
                build_list+=" &"
        new_build=Buildorders(writer=request.POST['writer'],headline=request.POST['headline'],buildorder=request.POST['buildorder'],username_id=request.user.id,explanation=request.POST['exp'],age=request.POST['age'],vote=1,build_list=build_list)
        new_build.save()
        return HttpResponseRedirect(reverse('basemap:index'))
    else:
        return render(request, 'builds/addbuild.html',{'user':user,})
@login_required(login_url='/login')       
def voteplus(request,build_id):
        if voters.objects.filter(user1=request.user.id,voted=build_id).exists():
            messages.error(request,'Zaten Oy Verdiniz')
            return redirect('builds:detail',build_id=build_id)
        else:
            build=Buildorders.objects.filter(pk=build_id)[0]
            build.vote+=1
            build.save()
            new_voter=voters(user1=request.user.id,voted=build_id)
            new_voter.save()
            return redirect('builds:detail',build_id=build_id)
@login_required(login_url='/login')       
def voteminus(request,build_id):
        if voters.objects.filter(user1=request.user.id ,voted=build_id).exists():
            messages.error(request,'Zaten Oy Verdiniz')
            return redirect('builds:detail',build_id=build_id)
        else:
            build=Buildorders.objects.filter(pk=build_id)[0]
            build.vote-=1
            build.save()
            new_voter=voters(user1=request.user.id,voted=build_id)
            new_voter.save()
            return redirect('builds:detail',build_id=build_id)
@login_required(login_url='/login') 
def mybuildorders(request):
    users_comments=comments.objects.filter(comuser_id=request.user.id,approved=True)
    users_builds=Buildorders.objects.filter(username_id=request.user.id)
    context={
        'users_builds':users_builds,
        'users_comments':users_comments,
    }
    return render(request,'builds/mybuildorders.html',context)
@login_required(login_url='/login') 
def changebuild(request,build_id):
    build = get_object_or_404(Buildorders, pk=build_id)
    if request.user.id == build.username_id:
        if request.method=='POST':
            build.headline=request.POST['headline']
            build.explanation=request.POST['exp']
            build.age=request.POST['age']
            build.buildorder=request.POST['buildorder']
            build.approved=False
            build_list=""
            for i in range(1,18):
                if request.POST['list%s' %i]:
                    listitem=request.POST['list%s' %i]
                    build_list+=str(listitem)+"&"
                else :
                    build_list+=" &"
            build.build_list=build_list
            build.save()
            messages.info(request,'Onay için gönderildi')
            return redirect('builds:mybuildorders')
        else:
            build_list_raw=Buildorders.objects.filter(pk=build_id)[0].build_list
            build_list_raw.split("&",)
            build_list=[]
            k=1
            for i in build_list_raw.split("&",):
                if i=='&' or i=="":
                   continue
                else :
                    build_list.append(tuple((i,k)))
                    k+=1
            context={
                'build':build,
                'build_list':build_list,
            }
            return render(request,'builds/changebuild.html',context)
    else:
        return redirect('builds:detail',build_id=build_id)
def search(request):
    if request.method=='POST':
        search_title=request.POST['search']
        search_list=Buildorders.objects.filter(headline__contains=search_title,approved=True)
        if len(search_list)>=1 :
            return render(request,'builds/results.html',{'search_list':search_list,})
        else:
            messages.error(request,"Malesef, böyle bir başlık yok")
            return redirect('builds:index')
    else:
        return redirect('builds:index')
@login_required(login_url='/login')
def deletebuild(request,build_id):
        if request.user.id==Buildorders.objects.filter(pk=build_id)[0].username_id:
            dele=Buildorders.objects.filter(pk=build_id).first()
            dele.delete()
            messages.warning(request,'Buildorder silindi')
            return redirect('builds:index')
        else:
            return redirect('builds:detail',build_id=build_id)
