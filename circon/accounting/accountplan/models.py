from django.db import models


class AccountPlan(models.Model):
    code = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.description

    class Meta:
        permissions = (
                ("to_access_accounting", "Puede acceder a contabilidad"),
            )
