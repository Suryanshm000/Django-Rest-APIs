from rest_framework import serializers
from firstApp.models import AndroidApp

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidApp
        fields = '__all__'