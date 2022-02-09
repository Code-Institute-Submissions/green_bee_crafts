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
        'stripe_public_key': 'pk_live_51JvilWL49WFTmKqyoqwpfSouotb2h3glqfKNasMumvK9b9FCWhRdbW1M0PfIOglBTIPsnVJqBbR5Bz9p9lq7b9xs00mZdKxq01'
    }

    return render(request, template, context)