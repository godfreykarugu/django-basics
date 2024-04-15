from django.urls import path

from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('testing/', views.testing, name='testing'),
    path('greetings/', views.greetings, name='greetings'),
    path('fruits/', views.fruits, name='fruits'),
    path('forloop/', views.forloop, name='forloop'),
    path('testing/details/<int:id>', views.details, name='details'),
]