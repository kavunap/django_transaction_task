from django import forms
from .models import Order, Item,OrderedList
from django.forms import inlineformset_factory

class OrderForm(forms.Form):
    pass
    # created_at = forms.CharField(label='Name', max_length=255)
    # email = forms.EmailField(label='Email')
    OrderFormset = inlineformset_factory(Order, OrderedList, fields=('order',))