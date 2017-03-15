from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):
    product_code  = models.CharField(max_length=100, null=True)

from oscar.apps.catalogue.models import *