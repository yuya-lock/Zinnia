from django.urls import path
from .views import IndexView, HomeView

urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('home', HomeView.as_view(), name='home')
]
