from django.db import models
from audit_log.models.fields import LastUserField
from audit_log.models.managers import AuditLog


class Category(models.Model):
    category = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    audit_log = AuditLog()

    def __str__(self):
        return self.category
