# store/forms.py

from django import forms

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100, label='Mike')
    email = forms.EmailField(label='saqibkhank805@gmail.com')
    address = forms.CharField(widget=forms.Textarea, label='Shipping Address')
