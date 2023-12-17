from django.urls import path
from . import views

urlpatterns = [
    path('realtime', views.realtime_summary, name='realtime_summary'),
    path('polish', views.polish, name='polish'),
]