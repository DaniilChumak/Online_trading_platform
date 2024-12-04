from rest_framework import serializers

from trading.models import Contacts, Product, Element


class ContactSerializer(serializers.ModelSerializer):
    """
    Класс-сериализатор для модели Contacts.
    """

    class Meta:
        """
        Мета-класс — это внутренний класс обслуживания сериализатора.
        Определяет необходимые параметры для работы сериализатора.
        """

        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Класс-сериализатор для модели Product.
    """

    class Meta:
        """
        Мета-класс — это внутренний класс обслуживания сериализатора.
        Определяет необходимые параметры для работы сериализатора.
        """

        model = Product
        fields = '__all__'


class ElementSerializer(serializers.ModelSerializer):
    """
    Класс-сериализатор для модели Element.
    """

    contacts = ContactSerializer(many=False, read_only=True, required=False)
    products = ProductSerializer(many=True, read_only=True, required=False)
    supplier = serializers.SlugRelatedField(required=False, queryset=Element.objects.all(), slug_field="title")

    class Meta:
        """
        Мета-класс — это внутренний класс обслуживания сериализатора.
        Определяет необходимые параметры для работы сериализатора.
        """

        model = Element
        fields = ['id', 'title', 'item', 'supplier', 'level', 'debt_to_supplier', 'date_of_creation', 'contacts', 'products',]
        read_only_fields = ('debt_to_supplier',)
