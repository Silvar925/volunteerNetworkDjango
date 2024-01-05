from django.shortcuts import render

def personalProfile(request):
    return render(request, 'personalProfile/profile.html')

def authentication(request):
    return render(request, 'personalProfile/authentication.html')