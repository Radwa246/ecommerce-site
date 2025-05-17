from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('confirmation/', views.confirmation, name='confirmation'),
]
