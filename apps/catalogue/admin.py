from django.contrib import admin

from oscar.core.loading import get_model, get_class

Product = get_model('catalogue', 'product')

admin.site.register(Product)
