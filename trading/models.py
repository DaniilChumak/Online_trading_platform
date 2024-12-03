from django.db import models

# определение переменной для удобства работы с полями модели
NULLABLE = {'blank': True, 'null': True}


class Element(models.Model):
    """
    Определяет поля таблицы базы данных, их свойства и ограничения.
    Элемент сети может быть любым из трех видов: завод, розничная сеть, ИП.
    """

    ITEM_CHOICES = (
        ('FACTORY', 'Завод'),
        ('RETAIL', 'Розничная сеть'),
        ('IE', 'ИП'),
    )

    LEVEL_CHOICES = (
        (0, 0),
        (1, 1),
        (2, 2),
    )

    title = models.CharField(max_length=150, unique=True, verbose_name='Название')
    item = models.CharField(max_length=50, choices=ITEM_CHOICES, verbose_name='Тип элемента сети')
    supplier = models.ForeignKey('self', max_length=100, **NULLABLE, default=None, on_delete=models.SET_DEFAULT, verbose_name='Поставщик')
    level = models.PositiveIntegerField(choices=LEVEL_CHOICES, verbose_name='Уровень')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Долг перед поставщиком')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        """
        Метод возвращает текстовое представление экземпляра модели.
        """

        return self.title

    class Meta:
        """
        Класс Meta содержит общее имя экземпляра модели в единственном и множественном числе
        в админ-панели.
        """

        verbose_name = 'Элемент сети'
        verbose_name_plural = 'Элементы сети'


class Contacts(models.Model):
    """
    Определяет поля таблицы базы данных, их свойства и ограничения.
    Присваивает каждому элементу сети свои контактные данные.
    """

    unit = models.OneToOneField(Element, on_delete=models.CASCADE, verbose_name='Элемент сети')
    email = models.EmailField(**NULLABLE, verbose_name='Электронная почта')
    country = models.CharField(max_length=100, **NULLABLE, verbose_name='Страна')
    city = models.CharField(max_length=150, **NULLABLE, verbose_name='Город')
    street = models.CharField(max_length=250, **NULLABLE, verbose_name='Улица')
    house = models.CharField(max_length=5, **NULLABLE, verbose_name='Дом')

    def __str__(self):
        """
        Метод возвращает текстовое представление экземпляра модели.
        """

        return f'{self.unit.title} - контакты'

    class Meta:
        """
        Класс Meta содержит общее имя экземпляра модели в единственном и множественном числе
        в админ-панели.
        """

        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    """
    Определяет поля таблицы базы данных, их свойства и ограничения.
    Указывает на принадлежность продукта конкретному элементу сети.
    """

    unit = models.ForeignKey(Element, on_delete=models.CASCADE, verbose_name='Элемент сети')
    title = models.CharField(max_length=150, verbose_name='Название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель продукта')
    release_date = models.DateField(verbose_name='Дата выпуска')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена')

    def __str__(self):
        """
        Метод возвращает текстовое представление экземпляра модели.
        """

        return self.title

    class Meta:
        """
        Класс Meta содержит общее имя экземпляра модели в единственном и множественном числе
        в админ-панели.
        """

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title',]
