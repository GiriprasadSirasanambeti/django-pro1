"""
URL configuration for jobquest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import login_view, logout_view, dashboard_view, add_job_view, edit_job_view, delete_job_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('job/board/', dashboard_view, name='job_board'),
    path('job/add/', add_job_view, name='add_job'),
    path('job/edit/<int:job_id>/', edit_job_view, name='edit_job'),
    path('job/delete/<int:job_id>/', delete_job_view, name='delete_job'),
    path('', login_view, name='home'),
]
