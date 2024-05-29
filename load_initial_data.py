import csv
import django
import os
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bleemeo_quote.settings.development")

django.setup()

from bleemeo_quote.models import Author, Quote  # noqa: E402

with open(settings.QUOTE_CSV_FILE, encoding="utf-8") as fd:
    reader = csv.reader(fd, delimiter=";")
    for row in reader:
        if row[1]:
            (author, created) = Author.objects.get_or_create(name=row[1])
        else:
            (author, created) = Author.objects.get_or_create(name="Unknown")
        Quote.objects.get_or_create(author=author, quote=row[0])
