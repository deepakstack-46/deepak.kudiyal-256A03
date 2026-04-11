from django.urls import path
from . import views

urlpatterns = [
    path('', views.position_list, name='position_list'),
    path('create/', views.position_create, name='position_create'),
    path('<int:pk>/update/', views.position_update, name='position_update'),
    path('<int:pk>/delete', views.position_delete, name='position_delete'),
]