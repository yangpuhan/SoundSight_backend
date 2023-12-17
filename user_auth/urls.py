from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('user_info', views.user_info, name='user_info'),
    path('realtime/begin', views.realtime_begin, name='realtime_begin'),
    path('realtime/middle', views.realtime_middle, name='realtime_middle'),
    path('realtime/end', views.realtime_end, name='realtime_end'),
]