from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Payment settings
stripe.api_key = settings.STRIPE_SECRET


"""
Require login (show login form when user press the post-button)
"""


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

# get info of what has been purchased:

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

# try except that create customer and charge using Stripe (Stripe uses cents or pennies therefore x100)

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
# give message to customer how it went with the purchase

            if customer.paid:
                messages.error(request, "Thank You for your purchase, your order will be delivered within 4 days.")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Payment failed -please try again.")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card, please try another one!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
