from django.urls import path
from .views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
]
from django.urls import path
from .views import dashboard, registrar_usuario

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('registro/', registrar_usuario, name='registro'),
]
from django.urls import path, include
from .views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('tareas/', include('tasks.urls')),
]
