from django.urls import path
from . import views

urlpatterns = [
     
     
    path('', views.form_view, name='form'),
    path('submit/', views.submit, name='submit'),
    path('submit1/', views.submit1, name='submit1'),
    path('Donator/', views.donator, name='Donator'),
    path('inNeed/', views.in_need, name='inNeed'),
    path('post/<str:pk>', views.post, name='post'),
    path('blogs/', views.blogs, name='blogs'),
    path('posting', views.posting, name='posting')
]