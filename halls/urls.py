from django.urls import path

from .views import (
    HallListView, HallDetailView, HallCreateView, HallUpdateView, HallDeleteView,
    ReviewListView, ReviewCreateView, ReviewDeleteView
)


app_name = 'halls'
urlpatterns = [
    path('hall_list/', HallListView.as_view(), name='hall_list'),
    path('hall_create/', HallCreateView.as_view(), name='hall_create'),
    path('hall_detail/<int:pk>', HallDetailView.as_view(), name='hall_detail'),
    path('hall_update/<int:pk>', HallUpdateView.as_view(), name='hall_update'),
    path('hall_delete/<int:pk>', HallDeleteView.as_view(), name='hall_delete'),
    path('review_list/<int:pk>', ReviewListView.as_view(), name='review_list'),
    path('review_create/<int:pk>', ReviewCreateView.as_view(), name='review_create'),
    path('review_delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
]