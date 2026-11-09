from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('post/novo/', views.criar, name='criar'),
    path('post/<int:pk>/', views.detalhe, name='detalhe'),
    path('post/<int:pk>/editar/', views.editar, name='editar'),
    path('post/<int:pk>/remover/', views.remover, name='remover'),
]