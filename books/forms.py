from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ["isbn"]

        widgets = {
            "isbn": forms.TextInput(attrs={"placeholder": "ISBN"})
        }