from django.urls import path
from .views import lista_tareas, crear_tarea, editar_tarea, eliminar_tarea

urlpatterns = [
    path('', lista_tareas, name='lista_tareas'),
    path('crear/', crear_tarea, name='crear_tarea'),
    path('editar/<int:pk>/', editar_tarea, name='editar_tarea'),
    path('eliminar/<int:pk>/', eliminar_tarea, name='eliminar_tarea'),
]
