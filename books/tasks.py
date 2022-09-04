from celery import shared_task
import requests
import json
from .models import Book, OpenApiReference
from celery.exceptions import Ignore


@shared_task
def get_reference_from_open_library(isbn):
    url_to_get="https://openlibrary.org/isbn/" + str(isbn) + ".json"
    r = requests.get(url_to_get)
    r_status = r.status_code
    if r_status == 200:
        response = json.loads(r.text)
        number_of_pages=response["number_of_pages"]
        title=response["title"]
        publish_date=response["publish_date"]
        book_to_complete=Book.objects.get(isbn=isbn)
        OpenApiReference.objects.update_or_create(
            book=book_to_complete, 
            number_of_pages=number_of_pages,
            title=title,
            publish_date=publish_date
            )
    else:
        raise Ignore()