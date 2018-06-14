from django.views.generic import ListView

from .exceptions import SortingServiceException
from .models import Book


class BookListView(ListView):
    """
    This view receives parameters and sorts the elements by them
    """
    model = Book
    template_name = 'book_list.html'
    queryset = Book.objects.all()

    def get_ordering(self):
        ordering = self.request.GET.get('ordering')
        if ordering:
            if 'null' in ordering:
                raise SortingServiceException
            else:
                return ordering.split(',')
