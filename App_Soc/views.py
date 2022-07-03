from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.http import HttpResponseRedirect

def manage_user(request):
    user_list = User.objects.all()
    return render(request, 'App_Soc/manage_user.html', context={'user_list': user_list})

def index(request):
    users = User.objects.all()
    return render(request, 'App_Soc/index.html', context={'users': users})

def user_detail(request, ic_no):
    user = User.objects.get(pk=ic_no)     # pk='primary key'
    return render(request, 'App_Soc/user_detail.html', context={'user': user})

def newUser_form(request):
    submitted = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pkob/manage_user/?submitted=True')
    else:
        form=UserForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'App_Soc/newUser_form.html', {'form':form, 'submitted':submitted})

def editUser_form(request, ic_no):
    submitted = False
    data = User.objects.get(pk=ic_no)
    form = UserForm(instance=data)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/pkob/manage_user/')

    context = {'form':form}
    return render(request, 'App_Soc/editUser_form.html', context)

def delete_user(request, ic_no):
    user = User.objects.get(pk=ic_no)
    user.delete()
    return redirect('/pkob/manage_user/')






