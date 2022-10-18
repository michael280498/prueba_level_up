from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_form, name='form-create'),
    path('list/', views.form_list, name='form-list'),
    
]