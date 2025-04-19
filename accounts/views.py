import sys

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Job

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(f"Authenticate result: {user}", file=sys.stderr) #debug output
        if user is not None:
            login(request, user)
            print(f"Logged in user: {user.username}", file=sys.stderr)  #debug output
            return redirect('job_board')  # Replace 'home' with your homepage URL later
        else:
            print("Authentication Failed", file=sys.stderr)  # Debug output
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')   # Redirect to login page after logout

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    jobs = Job.objects.filter(user=request.user)   # Add job listing to dashboard
    return render(request, 'accounts/dashboard.html', {'user': request.user, 'jobs': jobs})

def add_job_view(request):
    if request.method == 'POST' and request.user.is_authenticated:
        title = request.POST['title']
        description = request.POST['description']
        company = request.POST['company']
        Job.objects.create(title=title, description=description, company=company, user=request.user)
        return redirect('job_board') # Redirect back to dashboard
    return redirect('job_board')

def edit_job_view(request, job_id):
    if not request.user.is_authenticated:
        return redirect('login')
    job = Job.objects.get(id=job_id, user=request.user)
    if request.method == 'POST':
        job.title = request.POST['title']
        job.description = request.POST['description']
        job.company = request.POST['company']
        job.save()
        return redirect('job_board')
    return render(request, 'accounts/edit_job.html', {'job':job})

def delete_job_view(request, job_id):
    if not request.user.is_authenticated:
        return redirect('login')
    job = Job.objects.get(id=job_id, user=request.user)
    job.delete()
    return redirect('job_board')