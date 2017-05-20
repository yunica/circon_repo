from django.conf.urls import url, include
from rest_framework import routers
from .views import ProductsViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductsViewSet)

urlpatterns = [
                url(r'^api/', include(router.urls)),
              ]
