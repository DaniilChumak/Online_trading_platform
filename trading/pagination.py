from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    """Настройки пагинации для модели продукта."""

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100
