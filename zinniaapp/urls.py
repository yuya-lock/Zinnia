from django.urls import path
from .views import IndexView, HomeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home')
]
