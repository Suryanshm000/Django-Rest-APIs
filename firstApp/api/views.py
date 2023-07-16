from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, Http404
from .serializers import AppSerializer
from firstApp.models import AndroidApp
from rest_framework import viewsets
from rest_framework.schemas import AutoSchema
from rest_framework.compat import coreapi, coreschema
from rest_framework.decorators import action


@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def admin_home(request):
    
    app = AndroidApp.objects.all()
    serializer = AppSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def add_app(request):

    serializer = AppSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {'msg': 'App added'}
        return Response(data=data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_home(request):
    
    app = AndroidApp.objects.all()
    serializer = AppSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def app_detail(request, pk):

    app = get_object_or_404(AndroidApp, pk=pk)
    serializer = AppSerializer(app)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def app_delete(request, pk):

    try:
        app = AndroidApp.objects.get(id=pk)
        app.delete()
        data = {'msg': 'App deleted'}
        return Response(data=data, status=status.HTTP_200_OK)
    except AndroidApp.DoesNotExist:
        raise Http404
