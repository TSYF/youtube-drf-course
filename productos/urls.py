from django.urls import path
from productos.views import (
    ProductoDestroyAPIView,
    ProductoDetalleAPIView,
    ProductoListCreateAPIView,
    ProductoMixinAPIView,
    ProductoUpdateAPIView
)
from . import views

urlpatterns = [
    path('', ProductoListCreateAPIView.as_view(), name="product-list"),
    # path('', ProductoMixinAPIView.as_view()),
    # path('<int:pk>/', ProductoMixinAPIView.as_view())
    path('<int:pk>/', ProductoDetalleAPIView.as_view(), name="product-detail"),
    path('<int:pk>/update/', ProductoUpdateAPIView.as_view()),
    path('<int:pk>/delete/', ProductoDestroyAPIView.as_view())
]
