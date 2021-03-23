from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cats/', views.cats_index, name='cats'),
    path('cats/<int:cat_id>/', views.cats_show, name='cats_show')
]
