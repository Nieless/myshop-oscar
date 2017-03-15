from django import forms

from oscar.core.loading import get_class, get_model

Product = get_model('catalogue', 'Product')
BaseProductForm = get_class('catalogue.forms', 'ProductForm')


class ProductForm(BaseProductForm):
    class Meta:
        model = Product
        fields = '__all__'

