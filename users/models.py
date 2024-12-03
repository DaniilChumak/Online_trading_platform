from django.contrib.auth.models import AbstractUser
from django.db import models


# определение переменной для удобства работы с полями модели
NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """
    Определяет поля таблицы базы данных, их свойства и ограничения.
    Переопределяет поле username на email.
    """

    username = None

    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=150, verbose_name="Имя", **NULLABLE)
    last_name = models.CharField(max_length=200, verbose_name="Фамилия", **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        """
        Класс Meta содержит общее имя экземпляра модели в единственном и множественном числе
        в админ-панели.
        """

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("email",)
