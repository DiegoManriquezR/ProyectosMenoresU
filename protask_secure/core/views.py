from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('registro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return redirect('registro')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, 'Usuario creado correctamente')
        return redirect('login')

    return render(request, 'registro.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tasks.models import Tarea

@login_required
def dashboard(request):
    tareas = Tarea.objects.filter(usuario=request.user)

    context = {
        'total': tareas.count(),
        'pendientes': tareas.filter(estado='P').count(),
        'progreso': tareas.filter(estado='E').count(),
        'completadas': tareas.filter(estado='C').count(),
    }
    return render(request, 'dashboard.html', context)
