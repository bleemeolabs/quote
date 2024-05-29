from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Quote(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    quote = models.TextField()
