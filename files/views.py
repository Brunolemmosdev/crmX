from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, IsAuthenticated
from .filters import FileFilterClass

from .models import File, ContratosElementFile
from .serializers import FileSerializer, ContratosElementFileSerializer

from django.shortcuts import render

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [ IsAuthenticated, DjangoModelPermissions]
    rql_filter_class = FileFilterClass

    #""" IsAdminUser """ 

class ContratosElementFileViewSet(viewsets.ModelViewSet):
    queryset = ContratosElementFile.objects.all()
    serializer_class = ContratosElementFileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        element_id = self.request.query_params.get('element', None)
        if element_id:
            queryset = queryset.filter(element_id=element_id)
        return queryset 