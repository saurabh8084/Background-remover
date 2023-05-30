from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="Home"),
    path('remove-bg/', views.RemoveBGView.as_view(), name="RemoveBG"),
]
