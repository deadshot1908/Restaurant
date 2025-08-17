from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

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

@login_required
def profile_view(request):
    next_url = request.GET.get('next') or request.POST.get('next')
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            if next_url and next_url !='None':
                return redirect(next_url)

            return redirect('homepage')

    else:
        form = ProfileForm(instance = profile)
    
    return render(request,'user/profile.html',{
                                                'form':form,
                                                'username':request.user.username,
                                                'email':request.user.email,
                                                'next':next_url
                                                })