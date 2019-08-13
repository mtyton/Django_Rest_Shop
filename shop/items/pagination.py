from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class newLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50