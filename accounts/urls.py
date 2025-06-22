from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastroUser, name='cadastro'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
]
