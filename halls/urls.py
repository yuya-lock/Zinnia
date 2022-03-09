from django.urls import path

from .views import (
    HallListView,
)


app_name = 'halls'
urlpatterns = [
    path('hall_list/', HallListView.as_view(), name='hall_list'),
]