from rest_framework.routers import DefaultRouter
from productos.viewsets import ProductoViewSet, ProductoGenericViewSet

router = DefaultRouter()
router.register("productos", ProductoViewSet, basename="productos")


urlpatterns = router.urls