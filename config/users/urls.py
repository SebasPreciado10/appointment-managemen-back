# users/urls.py
from django.urls import path
from djoser.views import UserViewSet

user_create = UserViewSet.as_view({'post': 'create'})

urlpatterns = [
    path('', user_create, name='user-create'),  # /auth/users/
]
