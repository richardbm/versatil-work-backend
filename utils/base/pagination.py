from rest_framework import pagination


class PageNumberPagination(pagination.PageNumberPagination):
    """
    This Paginator allow to use pagination when the 'page'
    param is passed from the request. Without this param, the
    response is formatted without the pagination system.
    """
    page_size = 20

    # max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        if request.GET.get("page", None) is None:
            return None
        return super(PageNumberPagination, self).paginate_queryset(queryset, request, view)
