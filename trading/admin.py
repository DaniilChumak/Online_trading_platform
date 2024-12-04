from django.contrib import admin
from trading.models import Element, Product, Contacts


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    """
    Класс ElementAdmin наследуется от класса ModelAdmin. Определяет вывод полей экземпляра
    в админ-панель и возможность их редактирования.
    """

    list_display = ('title', 'item', 'level', 'supplier_link', 'debt_to_supplier',)
    list_filter = ('contacts__city',)
    search_fields = ('title', 'item',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """
        Функция создания действия очистки задолженности для выбранных элементов.
        """

        queryset.update(debt_to_supplier=0.00)

    clear_debt.short_description = 'Очистить задолженность'

    def supplier_link(self, obj):
        """
        Функция формирования ссылки на поставщика.
        """

        if obj.supplier:
            return f'<a href="/admin/trading_network/element/{obj.supplier.id}/">{obj.supplier.title}</a>'
        return 'Нет поставщика'
    supplier_link.short_description = 'Поставщик'
    supplier_link.allow_tags = True

    readonly_fields = ('supplier_link', 'date_of_creation',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Класс ProductAdmin наследуется от класса ModelAdmin. Определяет вывод полей экземпляра
    в админ-панель и возможность их редактирования.
    """

    list_display = ('unit', 'title', 'model', 'release_date', 'price',)
    list_filter = ('title',)
    search_fields = ('title', 'model',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """
    Класс ContactsAdmin наследуется от класса ModelAdmin. Определяет вывод полей экземпляра
    в админ-панель и возможность их редактирования.
    """

    list_display = ('unit', 'email', 'country', 'city', 'street', 'house',)
    list_filter = ('unit__title',)
    search_fields = ('unit__title', 'email', 'country', 'city', 'street',)