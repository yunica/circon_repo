from django.db import models
from django.contrib.auth.models import User

User.add_to_class('company', models.CharField(max_length=200, blank=True))
User.add_to_class('address', models.CharField(max_length=200, blank=True))
User.add_to_class('phone', models.CharField(max_length=100, blank=True))
User.add_to_class('rif', models.CharField(max_length=100, blank=True))
User.add_to_class('provider', models.BooleanField(default=False, blank=True))
User.add_to_class('customer', models.BooleanField(default=False, blank=True))
