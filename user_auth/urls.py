from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('userinfo', views.user_info, name='user_info'),
    path('audio', views.audio, name='audio'),
    path('settings', views.user_setting, name='settings'),
]