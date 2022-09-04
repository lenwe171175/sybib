from django.shortcuts import render, redirect

from books.forms import BookForm

from django.contrib import messages

from .models import Book

from django.views import View

from .tasks import get_reference_from_open_library

# Create your views here.

def index(request):
    return render(request, "books/index.html") 

class AddBook(View):
    form_class = BookForm
    template_name = "books/add_book.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form}) 

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
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
                get_reference_from_open_library.delay(isbn)
                messages.success(request, "Ajout réussi")
            return redirect(index)
        else:
            messages.error(request, "Une erreur est survenue")
        return render(request, self.template_name, {'form': form})