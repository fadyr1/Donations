from django.urls import path
from . import views

urlpatterns = [
     
     
    path('', views.form_view, name='form'),
    path('submit/', views.submit, name='submit'),
    path('submit1/', views.submit1, name='submit1'),
    path('Donator/', views.Donators, name='Donator'),
    path('inNeed/', views.inNeed, name='inNeed'),
]