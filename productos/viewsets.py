from rest_framework import mixins, viewsets

from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset         = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field     = "pk" # Default
    
    
class ProductoGenericViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
    ):
    queryset         = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field     = "pk" # Default
    