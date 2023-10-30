from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200, primary_key=True)
    publisher = models.CharField(max_length=200)
    page = models.IntegerField()
    quantity = models.IntegerField()
    fee = models.IntegerField()

    def __str__(self):
        return self.title


class Members(models.Model):
    members_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    mobile_no = models.BigIntegerField()
    debt = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    members_id = models.IntegerField()
    transaction_id = models.IntegerField()
    book_isbn = models.CharField(max_length=200)
    issue_date = models.DateField()
    return_date = models.DateField()
    number_of_days = models.IntegerField()
    total_rental_fees = models.IntegerField()
    is_returned = models.BooleanField(default=False)

    def __int__(self):
        return self.members_id


class LibraryBook(models.Model):
    bookID = models.IntegerField()
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    average_rating = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200, primary_key=True)
    isbn13 = models.CharField(max_length=200)
    language_code = models.CharField(max_length=200)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    quantity = models.IntegerField()
    fee = models.IntegerField()

    def __str__(self):
        return self.title
