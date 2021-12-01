from django.db import models


class Products(models.Model):
    user = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    weight = models.FloatField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Products'
