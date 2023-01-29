from django.db import models

from products.models import Product
from tables.models import Table

# Create your models here.

statuses = (("Pendiente", "pendiente"), ("Entregado", "entregado"))


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(max_length=50, choices=statuses)
    created_at = models.DateTimeField(auto_now_add=True)
    close = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.table} - {self.product} - {self.status} - {self.created_at}"
