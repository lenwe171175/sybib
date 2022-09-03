from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=200)
    scan_date = models.DateTimeField(auto_now_add=True)
    search_completed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.isbn

class Reference(models.Model):
    book = models.OneToOneField(Book, on_delete=CASCADE)