from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import requests
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# from rest_framework.schemas import AutoSchema
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import json

# Create your views here.
@login_required
@staff_member_required
def add_app(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        token, created = Token.objects.get_or_create(user=user)
        auth_token = token.key
        header = {'Authorization': 'Token ' + auth_token}
        response = requests.post('http://127.0.0.1:8000/api/add-app', headers=header, data=request.POST, files=request.FILES)
        response_content = response.content
        data = json.loads(response_content)

        if response.status_code == 201:
            return JsonResponse(data)
        else:
            return JsonResponse(data)

    return render(request, 'firstApp/add_app.html')

@login_required
def admin_home(request):
    user = User.objects.get(username=request.user.username)
    token, created = Token.objects.get_or_create(user=user)
    auth_token = token.key
    header = {'Authorization': 'Token ' + auth_token}
    response = requests.get('http://127.0.0.1:8000/api/admin-home', headers=header)
    response_content = response.content
    data = json.loads(response_content)

    if response.status_code == 200:
        return render(request, 'firstAPP/admin_home.html', {'android_apps': data})
    else:
        return JsonResponse(data, status=response.status_code)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('firstApp:login')
    else:
        form = UserCreationForm()

    return render(request, 'firstApp/signup.html', {'form': form}) 


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = {'username': username, 'password': password}
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            requests.post('http://127.0.0.1:8000/api/api-token-auth/', data=data)
            login(request, form.get_user())
            return redirect('firstApp:user_home')
    else:
        form = AuthenticationForm()
    return render(request, 'firstApp/login.html', {'form': form})


def profile(request):
    return render(request, 'firstApp/profile.html')


@login_required
def user_home(request):
    user = User.objects.get(username=request.user.username)
    token, created = Token.objects.get_or_create(user=user)
    auth_token = token.key
    header = {'Authorization': 'Token ' + auth_token}
    response = requests.get('http://127.0.0.1:8000/api/user-home', headers=header)
    response_content = response.content
    data = json.loads(response_content)
    if response.status_code == 200:
        return render(request, 'firstApp/home.html', {'android_apps': data})
    else:
        return JsonResponse(data, status=response.status_code)


def app_detail(request, pk):
    user = User.objects.get(username=request.user.username)
    token, created = Token.objects.get_or_create(user=user)
    auth_token = token.key
    header = {'Authorization': 'Token ' + auth_token}
    response = requests.get('http://127.0.0.1:8000/api/app/' + str(pk), headers=header)
    response_content = response.content
    data = json.loads(response_content)

    if response.status_code == 200:
        return render(request, 'firstApp/app_detail.html', context={'app': data})
    else:
        return JsonResponse(data, status=response.status_code)

# class CustomSchema(AutoSchema):
#     def __init__(self):
#         super(CustomSchema, self).__init__()
#     def get_manual_fields(self, path, method):
#         extra_fields = [
#             coreapi.Field('command', required=True, location='form', schema=String(), description='', type='', example=''), 
#             coreapi.Field('params', required=False, location='form', schema=String(), description='', type='', example='')
#         ]
#         manual_fields = super().get_manual_fields(path, method)
#         return manual_fields + extra_fields

