from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from . forms import LoginForm

# Create your views here.


def login(request):
    if request == "Post":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'],
                                password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated'/'successfully')
                else:
                    return HttpResponse('disable account')
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm 
    return render(request, 'users/login.html', {form:form})


