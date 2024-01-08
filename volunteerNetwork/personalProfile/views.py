from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm


def personalProfile(request):
    return render(request, 'personalProfile/profile.html')

def authentication(request):
    return render(request, 'personalProfile/authentication.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        retUser = User.objects.filter(email=email)
        
        if retUser.exists():
            user = retUser.first()
            surname = user.first_name
            name = user.last_name
            user_id = user.id

            request.session['fullname'] = {'surname': surname, 'name': name, 'id':user_id}

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('personalProfile')
            else:
                return render(request, 'personalProfile/authentication.html', {'error_message': 'Учетная запись отключена'})
        else:
            return render(request, 'personalProfile/authentication.html', {'error_message': 'Неверный логин или пароль'})

    return render(request, 'personalProfile/authentication.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personalProfile')
    else:
        form = UserCreationForm()

    return render(request, 'personalProfile/authentication.html', {'form': form})


def user_logout(request):
    logout(request) 
    return redirect('/')

def personalAccount(request):
    fullname = request.session.get('fullname', {})

    if request.user.is_authenticated:
        return render(request, 'personalAccount.html', {'fullname': fullname})
    else:
        return render(request, 'authorization.html', {'error_message': 'Пожалуйста, войдите в систему для доступа к личному кабинету.'})