"""
URL configuration for OnlyFans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from web import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.user_login, name='login'),
    path('acerca/', views.acerca),
    path('bienvenido/', views.bienvenido),
    path('contacto/', views.contacto),
    path('exito/', views.exito),
    path('logout/', views.sign_out, name='logout'),
    path('flan/', views.detalle_flan, name='detalle_flan'),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]

