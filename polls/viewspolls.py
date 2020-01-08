from django.shortcuts import render 
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def vote(request):
    return render(request,'vote.html')
def uservote(request):
    return render(request,'uservote.html')
    