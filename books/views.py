from django.shortcuts import render, redirect

from books.forms import BookForm

from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "books/index.html") 

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ajout réussi")
            return redirect(index)
        else:
            messages.error(request, "Une erreur est survenue")
    else:
        form = BookForm()
    return render(request, "books/add_book.html", {"form": form})