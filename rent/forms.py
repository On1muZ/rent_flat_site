from django import forms
from .models import Order, Comment

class orderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('title', 'adress', 'desc', 'price', 'img_outside', 'img_inside')
