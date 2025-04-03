from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account.models import CustomUser

def login_view(request):

    if request.user.is_authenticated:
        return redirect('home:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')

        else:
            raise Http404('something went wrong')

    return render(request, 'account/login.html', {})


def register_view(request):
    context = {'error':[]}

    if request.user.is_authenticated:
        return redirect('home:index')

    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')

        if password != conf_password:
            context['error'].append("Passwords do not match")
        elif CustomUser.objects.filter(username=username).exists():
            context['error'].append("UserName already taken")
        else:
            user = CustomUser.objects.create_user(username, email, password)
            login(request, user)
            return redirect('home:index')

    return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home:index')

def profile_view(request):
    if request.user.is_anonymous:
        return redirect('account:login')

    if request.method == 'POST':
        user = request.user
        data = {
            'first_name': request.POST.get('firstname'),
            'last_name': request.POST.get('lastname'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone'),
            'profile_image': request.FILES.get('file'),
        }
        for key, value in data.items():
            if value:
                setattr(user, key, value)

        if request.POST.get('remove_image'):
            user.profile_image.delete()
            user.profile_image = None

        user.save()
        return redirect('home:index')

    return render(request, 'account/profile.html', {})