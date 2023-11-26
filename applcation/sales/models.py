from django.db import models

# Create your models here.
class SalesData(models.Model):

    id = models.BigAutoField(primary_key=True, editable=False)
    purchaser_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_count = models.IntegerField()
    merchant_address = models.CharField(max_length=255)
    merchant_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"

    