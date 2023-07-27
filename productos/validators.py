from productos.models import Producto
from rest_framework import serializers, validators

# def validate_title(value):
#     qs = Producto.objects.filter(title__iexact=value)
#     if qs.exists():
#         raise serializers.ValidationError(f"{value} ya es un nombre de producto\n")
#     return value
def validate_title_no_hello(value: str):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} contiene 'hello', lo cual no está permitido.\n")
    return value

unique_producto_title = validators.UniqueValidator(queryset=Producto.objects.all(), lookup="iexact")