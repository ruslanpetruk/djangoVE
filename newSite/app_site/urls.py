# app_site/urls.py
from django.urls import path
from app_site import views
urlpatterns = [
    path(r'',views.HomePageView.as_view()),
]