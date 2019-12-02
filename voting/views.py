from django.shortcuts import redirect

def loginredirect(request):
    return redirect('/login/') 
