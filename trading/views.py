from rest_framework.viewsets import ModelViewSet

from trading.models import Element, Product, Contacts
from trading.pagination import ProductPagination
from trading.permissions import IsActiveEmployee
from trading.serializers import ElementSerializer, ProductSerializer, ContactSerializer


class ElementViewSet(ModelViewSet):
    """
    ViewSet для работы с моделью Element.
    """

    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    permission_classes = [IsActiveEmployee]

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get('country')
        if country:
            queryset = queryset.filter(country=country)
        return queryset


class ProductViewSet(ModelViewSet):
    """
    ViewSet для работы с моделью Product.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]
    pagination_class = ProductPagination


class ContactsViewSet(ModelViewSet):
    """
    ViewSet для работы с моделью Contacts.
    """

    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsActiveEmployee]