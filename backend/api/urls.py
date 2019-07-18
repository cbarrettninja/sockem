"""
URLs for the API

Note that all the paths below are preceded by
/api/
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as auth_views
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('api-token-auth/', auth_views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)