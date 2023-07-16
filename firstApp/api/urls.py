from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

urlpatterns = [
    path('admin-home', views.admin_home, name='admin_home'),
    path('add-app', views.add_app, name='add_app'),
    path('user-home', views.user_home, name='user_home'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('app/<int:pk>', views.app_detail, name='app_detail'),
    path('app-delete/<int:pk>', views.app_delete, name='app_delete'),
]