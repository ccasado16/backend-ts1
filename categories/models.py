from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title
