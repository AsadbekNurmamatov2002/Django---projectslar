from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm, UserRegistrForm
# Create your views here.

def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request,user)
                return HttpResponse('login yahshi bajarildi')
            else:
                return HttpResponse('nimadir xato!')
        else:
            return HttpResponse('xato code!')
    else:
        form=LoginForm()
    return render(request, 'login.html', {'form':form})

def Registr(request):
    if request.method=='POST':
        user_form=UserRegistrForm(request.POST)
        if user_form.is_valid():
            naw_user= user_form.save(commit=False)
            naw_user=user_form.set_password(
                user_form.cleaned_data['password']
            )
            naw_user.save()
            login(request, naw_user)
            return render(request, 'register_done.html', {'naw_user':naw_user})
        
    else:
        user_form=UserRegistrForm()
    return render(request, 'registr.html',{'user_form':user_form})


def logout_user(request):
    logout(request)
    return redirect('user_login')