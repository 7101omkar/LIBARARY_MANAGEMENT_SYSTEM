from datetime import datetime

import requests
import json
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Book, Members, Transaction, LibraryBook


# Create your views here.
def home(request):
    return render(request, 'home.html')


def bookView(request):
    books = Book.objects.all()
    context = {'book': books}
    return render(request, 'book.html', context)


def add_book_view(request):
    return render(request, 'add_book.html')


def add_book(request):
    title = request.POST["title"]
    author = request.POST["author"]
    isbn = request.POST["isbn"]
    publisher = request.POST["publisher"]
    page = request.POST["page"]
    quantity = request.POST["quantity"]
    fee = request.POST["fee"]

    book = Book(title=title,
                author=author,
                publisher=publisher,
                isbn=isbn,
                page=page,
                quantity=quantity,
                fee=fee)

    book.save()

    return HttpResponseRedirect("/book")


def edit_book_view(request):
    books = Book.objects.get(isbn=request.GET['bookid'])
    context = {'book': books}

    return render(request, 'edit_book.html', context)


def update_book(request):
    title = request.POST["title"]
    author = request.POST["author"]
    isbn = request.POST["isbn"]
    publisher = request.POST["publisher"]
    page = request.POST["page"]
    quantity = request.POST["quantity"]
    fee = request.POST["fee"]

    books = Book.objects.get(isbn=request.POST['bookid'])

    books.title = title
    books.author = author
    books.publisher = publisher
    books.isbn = isbn
    books.page = page
    books.quantity = quantity
    books.fee = fee
    books.save()
    return HttpResponseRedirect("/book")


def delete_book(request):
    books = Book.objects.get(isbn=request.GET['bookid'])
    books.delete()
    return HttpResponseRedirect("/book")


def membersView(request):
    members = Members.objects.all()
    context = {'members': members}
    return render(request, 'members.html', context)


def add_members_view(request):
    return render(request, 'add_members.html')


def add_members(request):
    members_id = request.POST["members_id"]
    name = request.POST["name"]
    email_id = request.POST["email_id"]
    mobile_no = request.POST["mobile_no"]

    members = Members(members_id=members_id,
                      name=name,
                      email_id=email_id,
                      mobile_no=mobile_no)

    members.save()

    return HttpResponseRedirect("/members")


def edit_members_view(request):
    members = Members.objects.get(members_id=request.GET.get('members_id'))
    context = {'members': members}

    return render(request, 'edit_members.html', context)


def edit_members(request):
    members_id = request.POST["members_id"]
    name = request.POST["name"]
    email_id = request.POST["email_id"]
    mobile_no = request.POST["mobile_no"]

    members = Members.objects.get(members_id=request.POST['members_id'])

    members.members_id = members_id
    members.name = name
    members.email_id = email_id
    members.mobile_no = mobile_no

    members.save()

    return HttpResponseRedirect("/members")


def delete_members(request):
    members = Members.objects.get(members_id=request.GET['members_id'])
    members.delete()
    return HttpResponseRedirect("/members")


def transactionView(request):
    transactions = Transaction.objects.all()
    var = []
    for i in transactions:
        reciept_id = i.transaction_id
        members_id = i.members_id
        book_isbn = i.book_isbn
        issue_date = i.issue_date
        return_date = i.return_date
        total_rental_fees = i.total_rental_fees
        oneMember = Members.objects.get(members_id=members_id)
        onebook = Book.objects.get(isbn=book_isbn)
        transData = TransactionData(reciept_id, members_id, oneMember.name, book_isbn, onebook.title, issue_date,
                                    return_date, total_rental_fees, i.is_returned)
        var.append(transData)
    context = {'transData': var}
    return render(request, 'transaction.html', context)


class TransactionData:
    def __init__(self, reciept_id, members_id, members_name, isbn, book_title, issue_date, return_date,
                 total_rental_fees, is_returned):
        self.reciept_id = reciept_id
        self.members_id = members_id
        self.members_name = members_name
        self.isbn = isbn
        self.book_title = book_title
        self.issue_date = issue_date
        self.return_date = return_date
        self.total_rental_fee = total_rental_fees
        self.is_returned = is_returned

        print(reciept_id, members_id, members_name, isbn, book_title, issue_date, return_date,
              total_rental_fees, is_returned)


def issue_book_view(request):
    return render(request, 'issue_book.html')


def issue_book(request):
    transactions = Transaction.objects.all()
    members_id = request.POST["members_id"]
    book_isbn = request.POST["book_isbn"]
    issue_date = request.POST["issue_date"]
    return_date = request.POST["return_date"]

    issue_date = datetime.strptime(issue_date, "%Y-%m-%d")
    return_date = datetime.strptime(return_date, "%Y-%m-%d")

    if return_date > issue_date:
        number_of_days = (return_date - issue_date).days
    else:
        number_of_days = 0

    try:
        onebook = Book.objects.get(isbn=book_isbn)
        onemember = Members.objects.get(members_id=members_id)
        fee = onebook.fee
        inventory = onebook.quantity

        total_rental_fees = int(number_of_days) * int(fee)

        if members_id == members_id and onemember.debt < 500:
            transaction = Transaction(members_id=members_id,
                                      book_isbn=book_isbn,
                                      issue_date=issue_date,
                                      return_date=return_date,
                                      number_of_days=number_of_days,
                                      total_rental_fees=total_rental_fees,
                                      transaction_id=len(transactions) + 1)

            transaction.save()
            updated_inventory = inventory - 1
            onebook.quantity = updated_inventory
            onebook.save()

            onemember.debt = onemember.debt + total_rental_fees
            onemember.save()

            return HttpResponseRedirect("/transactions")
        else:
            context = {'error': f"debt is more than 500 i.e {onemember.debt} to issue new book clear the debt first"}

            return render(request, 'debt.html', context)
    except:
        context = {'error': "Member Id or Book ISBN does not match from the Database"}
        return render(request, 'debt.html', context)

def return_book_view(request):
    return_book = Transaction.objects.get(transaction_id=request.GET.get('reciept_id'))
    reciept_id = return_book.transaction_id
    members_id = return_book.members_id
    book_isbn = return_book.book_isbn
    issue_date = return_book.issue_date
    return_date = return_book.return_date
    total_rental_fees = return_book.total_rental_fees
    oneMember = Members.objects.get(members_id=members_id)
    onebook = Book.objects.get(isbn=book_isbn)
    transData = TransactionData(reciept_id, members_id, oneMember.name, book_isbn, onebook.title, issue_date,
                                return_date, total_rental_fees, return_book.is_returned)
    print(transData)
    context = {'return_book': transData, 'form_title': 'Return Book'}
    print(context.get('return_book').members_id)
    return render(request, 'return_book.html', context)


def return_book(request):
    member_id = request.POST["member_id"]
    receipt_id = request.POST["rid"]
    is_returned = request.POST["is_returned"]
    book_isbn = request.POST["bIsbn"]

    onebook = Book.objects.get(isbn=book_isbn)
    onemember = Members.objects.get(members_id=member_id)
    single_transaction = Transaction.objects.get(transaction_id=receipt_id)

    single_transaction.is_returned = bool(is_returned)
    single_transaction.save()

    current_book_qty = onebook.quantity
    updated_book_qty = current_book_qty + 1
    onebook.quantity = updated_book_qty
    onebook.save()

    current_debt = onemember.debt
    updated_debt = current_debt - single_transaction.total_rental_fees
    if updated_debt > 0:
        onemember.debt = updated_debt
    else:
        onemember.debt = 0
    onemember.save()

    return HttpResponseRedirect("/transactions")


def search_book(request):
    search_term = request.POST['search_title']
    search_term1 = request.POST['search_author']
    try:
        book = Book.objects.filter(title__icontains=search_term, author__icontains=search_term1)
        context = {'book': book}
        return render(request, 'book.html', context)
    except Book.DoesNotExist:
        context = {"error_msg": "Book not found"}
        return render(request, 'search.html', context)


def import_data(request):
    response = requests.get('https://frappe.io/api/method/frappe-library?page=2&title=and')
    response_content = ApiMessage(**json.loads(response.content))
    list_of_books_dict = response_content.message
    var = []
    for single_book_dict in list_of_books_dict:
        new_single_book_dict = dict()
        for attribute_key in single_book_dict:
            trimmed_attribute_key = attribute_key.strip()
            new_single_book_dict.setdefault(trimmed_attribute_key)
            new_single_book_dict.update({trimmed_attribute_key: single_book_dict[attribute_key]})
        single_library_book = LibraryBook(**new_single_book_dict)
        single_library_book.quantity = 0 #setting default quantity
        single_library_book.fee = 0 #setting default fee
        single_library_book.save()
        var.append(single_library_book)
    context = {"response": var}
    return render(request, 'import_data.html', context)

class ApiMessage:
    def __init__(self, message):
        self.message = message
