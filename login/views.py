from django.shortcuts import render 
from django.shortcuts import redirect
from django.http import HttpResponse
from forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
# Create your views here.
def home(request):
    return render(request,'home.html')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=RegistrationForm() 
        
        args={'form':form}
        return render(request,'regform.html',args)
 
def profile(request):
    args={'user': request.user}
    return render(request,'profile.html',args)

def editprofile(request):
    if request.method=='POST':
        form=UserChangeForm(request.POST,isinstance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form=UserChangeForm(instance=request.user)
        args={'form': form}
        return render(request,'editprofile.html',args)