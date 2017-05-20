from django.db import models


class MyCompany(models.Model):
    name = models.CharField(max_length=200)
    rif = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        permissions = (
                ("to_access_configuration", "Puede acceder a configuracion"),
            )
