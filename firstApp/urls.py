from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='firstApp'

urlpatterns = [
    path('', views.user_home, name='user_home'),
    path('add-app', views.add_app, name="add_app"),
    path('admin-home', views.admin_home, name="admin_home"),
    path('user/signup/', views.signup, name='signup'),
    path('user/login/', views.user_login, name='login'),
    path('user/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/profile/', views.profile, name='user_profile'),
    path('app/<int:pk>', views.app_detail, name='app_detail')
]