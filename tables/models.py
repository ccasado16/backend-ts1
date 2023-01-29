from django.db import models

# Create your models here.


class Table(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return f"Table {self.number}"
