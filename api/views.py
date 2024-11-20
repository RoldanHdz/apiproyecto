from rest_framework import viewsets
from .models import Usuario, PerfilDeUsuario, Reporte, ApoyoEnReporte, ComentarioEnReporte, EntidadOficial
from .serializers import UsuarioSerializer, PerfilDeUsuarioSerializer, ReporteSerializer, ApoyoEnReporteSerializer, ComentarioEnReporteSerializer, EntidadOficialSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PerfilDeUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilDeUsuario.objects.all()
    serializer_class = PerfilDeUsuarioSerializer
    
class EntidadOficialViewSet(viewsets.ModelViewSet):
    queryset = EntidadOficial.objects.all()
    serializer_class = EntidadOficialSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class ApoyoEnReporteViewSet(viewsets.ModelViewSet):
    queryset = ApoyoEnReporte.objects.all()
    serializer_class = ApoyoEnReporteSerializer

class ComentarioEnReporteViewSet(viewsets.ModelViewSet):
    queryset = ComentarioEnReporte.objects.all()
    serializer_class = ComentarioEnReporteSerializer


