from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('login/submit', views.submit_login, name='submit_login'),
    path('logout/', views.logout_user, name='logout'),
]
