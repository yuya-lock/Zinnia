from django.urls import path

from .views import (
    HomeView, RegistUserView, UserLoginView, UserLogoutView, UserDetailView, activate_user,
    UserUpdateView
)


app_name = 'accounts'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('regist/', RegistUserView.as_view(), name='regist'),
    path('activate_user/<uuid:token>', activate_user, name='activate_user'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    path('user_logout/', UserLogoutView.as_view(), name='user_logout'),
    path('user_detail/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user_update/<int:pk>', UserUpdateView.as_view(), name='user_update'),
]
