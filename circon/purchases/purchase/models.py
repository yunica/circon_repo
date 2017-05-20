from django.db import models
from django.contrib.auth.models import User
from audit_log.models.fields import LastUserField
from audit_log.models.managers import AuditLog


class Purchase(models.Model):
    date_create = models.DateField(auto_now_add=True)
    date_purchase = models.DateField(null=True, blank=True)
    n_purchase = models.AutoField(primary_key=True)
    provider = models.ForeignKey(User)
    applicant = models.CharField(max_length=100, blank=True)
    observation = models.TextField(max_length=250, blank=True)
    base = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                               blank=True)
    iva = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                              blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                blank=True)
    status = models.CharField(max_length=1, default='0', blank=True)

    audit_log = AuditLog()

    def __str__(self):
        return self.date_purchase.strftime('%d-%m-%Y')

    class Meta:
        permissions = (
                ("to_access_purchase", "Puede acceder a compras"),
            )


class PurchaseDetail(models.Model):
    relationship = models.ForeignKey(Purchase)
    products = models.ForeignKey('products.Products')
    quantity = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                blank=True)
    total_product = models.DecimalField(max_digits=10, decimal_places=2,
                                        null=True, blank=True)
    quan_purchase = models.DecimalField(max_digits=10, decimal_places=2,
                                       null=True, blank=True)
    audit_log = AuditLog()
