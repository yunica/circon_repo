from django.conf.urls import url
from .views import Backup


urlpatterns = [
                url(r'^Backup$', Backup.as_view(), name='backup'),
              ]
