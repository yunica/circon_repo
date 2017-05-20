from django.db import models
from audit_log.models.fields import LastUserField
from audit_log.models.managers import AuditLog


def content_file_products(instance, filename):
    return 'warehouse/products/{0}/{1}'.format(instance, filename)


class Products(models.Model):
    products = models.CharField(max_length=100)
    measure = models.ForeignKey('units_measures.UnitsMeasures')
    quantity = models.DecimalField(max_digits=100, default='0',
                                   decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=100, default='0', decimal_places=2,
                                blank=True)
    description = models.TextField(max_length=250, blank=True)
    category = models.ForeignKey('category.Category')
    image = models.ImageField(upload_to=content_file_products, blank=True)
    active = models.BooleanField(default=True)

    audit_log = AuditLog()

    def __str__(self):
        return self.products

    class Meta:
        permissions = (
                ("to_access_warehouse", "Puede acceder a almacen"),
                ("add_entry", "Puede agregar entrada"),
                ("update_entry", "Puede actualizar entrada"),
                ("delete_entry", "Puede eliminar entrada"),
                ("add_exit", "Puede agregar salida"),
                ("update_exit", "Puede actualizar salida"),
                ("delete_exit", "Puede eliminar salida"),
                ("to_access_inventory", "Puede acceder a inventario"),
                ("to_access_request", "Puede acceder a solicitudes"),
                ("to_access_search", "Puede acceder a busquedas"),
            )
