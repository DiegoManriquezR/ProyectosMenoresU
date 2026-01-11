from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarea
from .forms import TareaForm

@login_required
def lista_tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'tasks/lista.html', {'tareas': tareas})

@login_required
def crear_tarea(request):
    form = TareaForm(request.POST or None)
    if form.is_valid():
        tarea = form.save(commit=False)
        tarea.usuario = request.user
        tarea.save()
        return redirect('lista_tareas')
    return render(request, 'tasks/form.html', {'form': form, 'titulo': 'Nueva tarea'})

@login_required
def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    form = TareaForm(request.POST or None, instance=tarea)
    if form.is_valid():
        form.save()
        return redirect('lista_tareas')
    return render(request, 'tasks/form.html', {'form': form, 'titulo': 'Editar tarea'})

@login_required
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    return render(request, 'tasks/eliminar.html', {'tarea': tarea})
