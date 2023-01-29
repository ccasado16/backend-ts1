from django.db import models

from tables.models import Table

# Create your models here.

payment_types = (
    ("Tarjeta", "tarjeta"),
    ("Efectivo", "efectivo"),
)

statuses = (
    ("Pendiente", "pendiente"),
    ("Pagado", "pagado"),
)


class Payment(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_type = models.CharField(max_length=50, choices=payment_types)
    status = models.CharField(max_length=50, choices=statuses)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.table} - {self.total_payment} - {self.payment_type} - {self.status} - {self.created_at}"
