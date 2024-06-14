from django.contrib.admin.templatetags.admin_list import pagination
from rest_framework import pagination


class ActivityPaginator(pagination.PageNumberPagination):
    page_size = 5