from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileForm, SupportForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Profile, Book
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def register_view(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user  # Make sure 'User' is the correct field name
            profile.save()

            messages.success(request, "Account created successfully")
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()

    return render(request, 'core/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
           
            profile =  Profile.objects.get(user=user)

            #redirect based on role
            if profile.role == 'student' :
                return redirect('student_dashboard')
            elif profile.role == 'admin':
                return redirect('admin_dashboard')
        else:                                                                                 # M...V..T
            messages.error(request, "Invalid username or password")
    else:
        form =AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

#handle student_dashboard view
@login_required
def student_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'core/student_dashboard.html',
    {'profile':profile})

# Handle the logout_view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('login')

    # admin_dashboard
def admin_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    if profile.role != 'admin':
        HttpResponseForbidden("You are not authorized to view this page")
    
    users = Profile.objects.filter(role='student') #view all students
    
    return render(request, 'core/admin_dashboard.html',{
        'admin' : profile,
        'users' : users
    })


@login_required
def view_books(request):
    books = Book.objects.filter(available=True)
    return render(request, 'core/view_books.html', {'books': books})


@login_required
def support_view(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            messages.success(request, "Support Message sent!")
    else:
        form = SupportForm()
    return render(request, 'core/support.html', {'form':form})