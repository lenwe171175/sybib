from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=200)
    scan_date = models.DateTimeField(auto_now_add=True)
    quantity= models.IntegerField(default=1)
    search_completed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.isbn

class OpenApiReference(models.Model):
    book = models.OneToOneField(Book, on_delete=CASCADE)
    publisher = models.CharField(max_length=250)
    number_of_pages = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    publish_date=models.CharField(max_length=250)

    def __unicode__(self):
        return self.book