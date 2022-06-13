from django.urls import path
from prog_auth import views

app_name = 'prog_auth'

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('home/', views.Home, name='home'),
    path('logout/', views.Logout, name='logout'),
]