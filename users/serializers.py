from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя."""

    class Meta:
        """
        Мета-класс — это внутренний класс обслуживания сериализатора.
        Определяет необходимые параметры для работы сериализатора.
        """

        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class LoginSerializer(serializers.ModelSerializer):
    """Сериализатор для аутентификации пользователя."""

    email = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        """
        Мета-класс — это внутренний класс обслуживания сериализатора.
        Определяет необходимые параметры для работы сериализатора.
        """

        model = User
        fields = ["email", "password",]

    def create(self, validated_data):
        """
        Функция создания переопределяет метод родительского класса. Принимает значения validated_data в качестве параметров.
        Аутентифицирует экземпляр класса User в соответствии с полученными значениями, вызывает AuthenticationFailed
        исключение, если в базе данных нет информации о пользователе или неверные данные. Возвращает найденный объект.
        """

        user = authenticate(email=validated_data["email"], password=validated_data["password"])
        if user is None:
            raise AuthenticationFailed
        return user
