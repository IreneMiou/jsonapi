from django.db import models


class Quotes(models.Model):
    quote = models.TextField()
    category = models.CharField(max_length=200, null=True, blank=True)
