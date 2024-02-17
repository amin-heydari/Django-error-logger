from django.urls import path

from . import views

urlpatterns = [
    path('', views.error_view),
    path('api/', views.APIErrorView.as_view())
]
