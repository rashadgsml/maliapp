from django.urls import path
from .view import UserDetail, UserList

app_name = 'users'

urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    path('user-detail/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]