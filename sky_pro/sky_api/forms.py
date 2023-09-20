from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    orders_current_month = forms.IntegerField(label='Количество заказов за текущий месяц', required=False)
    orders_last_month = forms.IntegerField(label='Количество заказов за прошлый месяц', required=False)

    class Meta:
        model = Product
        fields = ['name', 'category', 'is_active', 'price']