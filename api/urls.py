from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, PerfilDeUsuarioViewSet, ReporteViewSet, ApoyoEnReporteViewSet, ComentarioEnReporteViewSet, EntidadOficialViewSet


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'perfiles', PerfilDeUsuarioViewSet)
router.register(r'entidades', EntidadOficialViewSet)
router.register(r'reportes', ReporteViewSet)
router.register(r'apoyos', ApoyoEnReporteViewSet)
router.register(r'comentarios', ComentarioEnReporteViewSet)


urlpatterns = router.urls
