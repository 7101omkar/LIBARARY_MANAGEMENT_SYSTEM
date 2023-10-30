from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # to render homepage
    path('book', views.bookView, name='bookView'),  # to render list of book page
    path('add_book_view', views.add_book_view, name='add_book_view'),  # to render add book details form page
    path('add_book', views.add_book, name='add_book'),  # to add book details
    path('edit_book', views.edit_book_view, name='edit_book_view'),  # to render edit book form page
    path('edit_book/update', views.update_book, name='update_book'),  # to update book details
    path('delete_book', views.delete_book, name='delete_book'),  # to delete book details

    path('members', views.membersView, name='membersView'),  # to render list of book page
    path('add_members_view', views.add_members_view, name='add_members_view'), # to render add members details form page
    path('add_members', views.add_members, name='add_members'),  # to add members details
    path('edit_members', views.edit_members_view, name='edit_members_view'),  # to render edit members form page
    path('edit_members/update', views.edit_members, name='edit_members'),  # to update members details
    path('delete_members', views.delete_members, name='delete_members'),  # to delete members details

    path('transactions', views.transactionView, name='transactionView'),  # to render list of transaction page
    path('issue_book_view', views.issue_book_view, name='issue_book_view'),  # to render issued books form page
    path('issue_book', views.issue_book, name='issue_book'),  # to issue books
    path('return_book', views.return_book_view, name='return_book_view'),  # to render returned books form page
    path('return_book/update', views.return_book, name='return_book'),  # to return books

    path('search_book', views.search_book, name='search_book'),  # to render returned books form page
    path('import_data', views.import_data, name='import_data'), # to render imported data
]
