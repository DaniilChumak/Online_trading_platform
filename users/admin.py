from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Определяет вывод полей экземпляра в панель администрирования
    и возможность их редактирования.
    """

    list_display = (
        "id",
        "email",
    )
    list_filter = (
        "id",
        "email",
    )