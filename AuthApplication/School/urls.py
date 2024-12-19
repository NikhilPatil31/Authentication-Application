from django.urls import path, include
from .views import StudentApi

urlpatterns = [
    # path('profile/',views.DashboardView.as_view(), name='dashboard'),
    path('',StudentApi.as_view())
]