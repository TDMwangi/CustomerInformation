from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllCustomers, name='all_customers'),
    path('<int:pk>', views.SingleCustomer, name='single_customer')
]