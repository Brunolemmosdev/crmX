from rest_framework import serializers
from .models import File, ContratosElementFile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class ContratosElementFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratosElementFile
        fields = '__all__'