from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FileViewSet, ContratosElementFileViewSet

router = DefaultRouter()
router.register('file', FileViewSet)
router.register('contratos/(?P<element_id>[^/.]+)/documentos', ContratosElementFileViewSet, basename='contratos-documentos')

urlpatterns = [
    path('', include(router.urls)),
   
]