from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .models import Flan

def index(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes})

def acerca(request):
    return render(request, 'acerca.html')

def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'bienvenido.html', {'flanes_privados': flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('exito')
            return HttpResponseRedirect('/exito')
            contact_form = ContactForm.objects.create(**form.cleaned_data)
    else:
        form = ContactFormForm()
    return render(request, 'contacto.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('index') 
            except:
                return HttpResponse("El usuario ya existe")
        return HttpResponse("Las contraseñas no coinciden")

def sign_out(request):
    logout(request)
    return redirect('/')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST["username"],password=request.POST["password"])
        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm,'error':"El usuario o contraseña son incorrectos"})
        else:
            login(request,user)
            return redirect('/')

def detalle_flan(request, flan_id):
    flan = get_object_or_404(Flan, id=flan_id)
    return render(request, 'detalle_flan.html', {'flanes': flan})