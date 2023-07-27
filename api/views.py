# Yes rest framework
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from productos.serializers import ProductoSerializer



@api_view(["POST"])
def api_home(request, *args, **kwargs):
    data = request.data

    serializer = ProductoSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status.HTTP_200_OK)
    