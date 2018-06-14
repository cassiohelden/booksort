from django.core.management import BaseCommand

from book.models import Book


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Book block create
        book1 = Book.objects.create(title='Java How to Program', author='Deitel & Deitel', edition_year=2007)
        book2 = Book.objects.create(title='Patterns of Enterprise Application Architecture', author='Martin Fowler',
                                    edition_year=2002)
        book3 = Book.objects.create(title='Head First Design Patterns', author='Elisabeth Freeman', edition_year=2004)
        book4 = Book.objects.create(title='Internet & World Wide Web: How to program', author='Deitel & Deitel',
                                    edition_year=2007)

        self.stdout.write('Book1 created with title {}'.format(book1.title))
        self.stdout.write('Book2 created with title {}'.format(book2.title))
        self.stdout.write('Book3 created with title {}'.format(book3.title))
        self.stdout.write('Book4 created with title {}'.format(book4.title))



