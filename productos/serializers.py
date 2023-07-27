from rest_framework.reverse import reverse
from rest_framework import serializers
from productos.validators import validate_title_no_hello, unique_producto_title
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url    = serializers.SerializerMethodField(read_only=True)
    url         = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        lookup_field="pk"
    )
    # email       = serializers.EmailField(write_only=True)
    # email       = serializers.EmailField(source="user.email", write_only=True) # Foreign key thingy
    title       = serializers.CharField(validators=[ validate_title_no_hello, unique_producto_title ])
    name        = serializers.CharField(source="title", read_only=True)
    # user        = 
    
    class Meta:
        model = Producto
        fields = [
            # "user",
            "url",
            "edit_url",
            # "email",
            "name",
            "id",
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount"
        ]

    

    # def validate_title(self, value):
    #     qs = Producto.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} ya es un nombre de producto\n")
    #     return value
    
    # def validate_title(self, value):
    #     request = self.context.get("user")
    #     user    = request.user
    #     qs      = Producto.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} ya es un nombre de producto\n")
    #     return value


    def create(self, validated_data: dict):
        # return Producto.objects.create(**validated_data)
        # email = validated_data.pop("email")
        obj = super().create(validated_data)
        # print(email, obj)
        return obj

    def update(self, instance: Producto, validated_data: dict):
        # instance.title = validated_data.get("title")
        # return instance
        # email = validated_data.pop("email")
        return super().update(instance, validated_data)


    def get_edit_url(self, obj: Producto):

        request = self.context.get("request")

        if request in (None, False):
            return request

        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    # For using different property names a get_[p name] method is needed.
    def get_my_discount(self, obj: Producto):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Producto):
            return None
        
        
        return obj.get_discount()