from django.db import models

# Create your models here.
class Invoice(models.Model):
    date=models.DateField(auto_now_add=True)
    customer_name=models.CharField(max_length=1024,null=False)


class InvoiceDetails(models.Model):
    invoice_id=models.ForeignKey(Invoice,null=True,related_name='details',on_delete=models.CASCADE)
    description=models.TextField()
    quantity=models.FloatField()
    unit_price=models.FloatField()
    price=models.FloatField()
