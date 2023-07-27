from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Producto(models.Model):
    id      = models.AutoField("ID del producto", primary_key=True)
    user    = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title   = models.CharField("Título del producto", max_length=120)
    content = models.TextField("Descripción textual del producto", blank=True, null=True)
    price   = models.DecimalField("Precio del producto en USD", max_digits=15, decimal_places=2, default=9.99)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * .8)

    def get_discount(self):
        return .22