from rest_framework.routers import DefaultRouter
from ecommerce_tienda.views import ProductosViewSet

router = DefaultRouter()

router.register(r'products', ProductosViewSet, basename='products')

urlpatterns = router.urls