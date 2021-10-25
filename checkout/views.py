from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JoQ0SAtpkXtrAyMOM7XOiRB9gT8pNBVQum3J6rmFcguyEpYP07WLxZCIFQK9MzTL44g00RrE4F2Tt7ZnQOuDDhC00wkK9ZP8B',
    }

    return render(request, template, context)
