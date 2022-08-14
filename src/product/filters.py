import django_filters
from django import forms
from product.models import Product, Variant, ProductVariant


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(widget=forms.TextInput(
        attrs={
            "placeholder": "Product Title",
            "class": "form-control",
            "max_length":"255"
        }
    ))
    productvariant = django_filters.ModelChoiceFilter(
        label='Select A Variant',
        queryset=ProductVariant.objects.all().distinct(),  
        widget=forms.Select(
            attrs={
                "placeholder": "Select A Variant",
                "class": "form-control",
            }
    ))

    class Meta:
        model = Product
        fields = [
            'title',
            'productvariant',
            'created_at',
        ]
