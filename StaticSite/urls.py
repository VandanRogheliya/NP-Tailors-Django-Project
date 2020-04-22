from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('customerMeasurements', views.customerMeasurements,
         name='customerMeasurements'),

    path('dashboard', views.dashboard, name='dashboard'),

    path('resetPassword', views.resetPassword, name='resetPassword'),

    path('Signin', views.Signin, name='Signin'),

    path('Signout', views.Signout, name='Signout'),

    path('', include('django.contrib.auth.urls')),

    path('addCustomer', views.addCustomer, name='addCustomer'),

    path('edit', views.edit, name='edit'),


    path('', views.index, name='index')
]
