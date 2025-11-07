from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('challenges/', views.challenges, name='challenges'),
    path('socials/', views.socials, name='socials'),
]