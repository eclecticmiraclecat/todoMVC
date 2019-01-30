from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<todo_id>', views.delete, name='delete'),
    path('cross_off/<todo_id>', views.cross_off, name='cross_off'),
    path('uncross/<todo_id>', views.uncross, name='uncross'),
    path('active/', views.active, name='active'),
    path('completed/', views.completed, name='completed'),
    path('clear_completed/', views.clear_completed, name='clear_completed'),
]
