# store/forms.py

from django import forms

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your name: ')
    email = forms.EmailField(label='Your email: ')
    address = forms.CharField(widget=forms.Textarea, label='Shipping Address')
