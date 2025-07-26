from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth import login, authenticate

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    return render(request, 'registration/logged_out.html')

def home(request):
    return render(request, 'user_home.html')

def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance = profile)
    
    return render(request,'user/profile.html',{
                                                   'form':form,
                                                   'username':request.user.username,
                                                   'email':request.user.email
                                                   })