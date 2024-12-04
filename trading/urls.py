from django.urls import path, include
from rest_framework.routers import DefaultRouter

from trading.apps import TradingConfig
from trading.views import ElementViewSet, ProductViewSet, ContactsViewSet

app_name = TradingConfig.name

router = DefaultRouter()
router.register(r'elements', ElementViewSet, basename='element')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'contacts', ContactsViewSet, basename='contacts')

urlpatterns = [
    path('', include(router.urls)),
]
