# from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import CheckoutForm

def home(request):
    return render(request, 'store/cart.html')

def checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']

            # Send email
            send_mail(
                'Order Confirmation',
                f'Thank you {name}! Your order will be shipped to:\n{address}',
                'your_email@gmail.com',  # Replace with your Gmail
                [email],
                fail_silently=False,
            )

            return render(request, 'store/order_success.html', {'name': name})
    else:
        form = CheckoutForm()

    return render(request, 'store/checkout.html', {'form': form})

def confirmation(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        card = request.POST.get('card')

        return render(request, 'store/confirmation.html', {
            'address': address,
            'card': card
        })
    return render(request, 'store/confirmation.html')

