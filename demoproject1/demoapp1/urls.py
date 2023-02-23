from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo'),
   # path('contact/', views.contact, name='contact'),
   #path('details/', views.details, name='details'),
    #path('about/', views.about, name='about'),
    #path('thanks/', views.thanks, name='thanks'),
    #path('math/', views.math_op, name='math_op'),

]