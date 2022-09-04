from django.shortcuts import render, redirect

from books.forms import BookForm

from django.contrib import messages

from .models import Book

# Create your views here.

def index(request):
    return render(request, "books/index.html") 

def add_book_scan(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            isbn=form.isbn
            if Book.objects.filter(isbn=isbn).count() == 1:
                target_book=Book.objects.get(isbn=isbn)
                target_book.quantity+=1
                target_book.save()
                messages.success(request, "ISBN déjà existant - quantité modifiée")
            else:
                form.save()
                messages.success(request, "Ajout réussi")
            return redirect(index)
        else:
            messages.error(request, "Une erreur est survenue")
    else:
        form = BookForm()
    return render(request, "books/add_book_scan.html", {"form": form})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            isbn=form.isbn
            if Book.objects.filter(isbn=isbn).count() == 1:
                target_book=Book.objects.get(isbn=isbn)
                target_book.quantity+=1
                target_book.save()
                messages.success(request, "ISBN déjà existant - quantité modifiée")
            else:
                form.save()
                messages.success(request, "Ajout réussi")
            return redirect(index)
        else:
            messages.error(request, "Une erreur est survenue")
    else:
        form = BookForm()
    return render(request, "books/add_book.html", {"form": form})