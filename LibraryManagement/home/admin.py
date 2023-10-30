from django.contrib import admin
from .models import Book, Members, Transaction, LibraryBook

# Register your models here.

admin.site.register(Book)
admin.site.register(Members)
admin.site.register(Transaction)
admin.site.register(LibraryBook)