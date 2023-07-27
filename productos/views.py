from rest_framework import generics, mixins, permissions, authentication
from api.mixins import IsStaffEditorPermissionMixin, UserQuerySetMixin
from .models import Producto
from .serializers import ProductoSerializer
from api.permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication

# Create your views here.


# class ProductoCreateAPIView(generics.CreateAPIView):
#     queryset = Producto.objects.all()
#     serializer_class = ProductoSerializer

#     def perform_create(self, serializer: ProductoSerializer):
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')

#         if not content:
#             content = title
        
#         print(serializer.validated_data)
#         return serializer.save(content=content)

class ProductoListCreateAPIView(
    generics.ListCreateAPIView,
    IsStaffEditorPermissionMixin,
    UserQuerySetMixin
):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    # Not needed because DEFAULT_AUTHENTICATION_CLASSES is set.
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication
    # ]
    # permission_classes = [ permissions.IsAdminUser, IsStaffEditorPermission ] # Not needed because of IsStaffEditorPermissionMixin

    def perform_create(self, serializer: ProductoSerializer):
        # email = serializer.validated_data.pop("email")
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if not content:
            content = title
        
        # print(email, serializer.validated_data)
        return serializer.save(user=self.request.user, content=content)

    # Not needed because of UserQuerySetMixin
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     request = self.request

    #     return qs.filter(user=request.user)
    
class ProductoDetalleAPIView(
    generics.RetrieveAPIView,
    IsStaffEditorPermissionMixin,
    UserQuerySetMixin
):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    # permission_classes = [ permissions.IsAdminUser, IsStaffEditorPermission ] # Not needed because of IsStaffEditorPermissionMixin
    # lookup_field = "pk"

class ProductoUpdateAPIView(
    generics.UpdateAPIView,
    IsStaffEditorPermissionMixin,
    UserQuerySetMixin
):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [ permissions.IsAdminUser, IsStaffEditorPermission ] # Not needed because of IsStaffEditorPermissionMixin
    lookup_field = "pk"

    def perform_update(self, serializer: ProductoSerializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title
            

class ProductoDestroyAPIView(
    generics.DestroyAPIView,
    IsStaffEditorPermissionMixin,
    UserQuerySetMixin
):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [ permissions.IsAdminUser, IsStaffEditorPermission ] # Not needed because of IsStaffEditorPermissionMixin
    lookup_field = "pk"
    
    def perform_destroy(self, serializer: ProductoSerializer):
        # Anything I need to do with the instance
        
        super().perform_destroy(serializer)

class ProductoMixinAPIView(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView
    ):
    
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = "pk"
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        


    # ======= PRE-ACTION STUFF =======

    def perform_create(self, serializer: ProductoSerializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if not content:
            content = title
        
        print(serializer.validated_data)
        return serializer.save(content=content)

    def perform_update(self, serializer: ProductoSerializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title

    def perform_destroy(self, serializer: ProductoSerializer):
        # Anything I need to do with the instance
        
        super().perform_destroy(serializer)