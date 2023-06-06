from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def loginView(request):
    context = {
        'page_title': 'LOGIN'
    }
    
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('store:store')
        else:
            return render(request, 'login.html', context)


    if request.method == 'POST':
        name_login = request.POST['username']
        pass_login = request.POST['password']

        user = authenticate(request, username=name_login, password=pass_login)
        if user is not None:
            login(request,user)
            return redirect('store:store')
        else:
            return redirect('login')

@login_required
def logoutView(request):
    context = {
        'page_title':'LOGOUT'
    }

    if request.method == 'POST':
        if request.POST['logout'] == 'Submit':
            logout(request)
        return redirect('store:store')
    
    return render(request, 'logout.html', context)