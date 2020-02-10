from django import forms
from .models import Order


"""
In the Django form required=False this is for not transmitting plain text
through the browser -instead it is handled by Stripe Javascript (for Security)


The form widget "hiddenInput means that something will be put in to the form but it will
be hidden for the user to see.
"""

# Paymentform


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


# Order form


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'street_address', 'postcode', 
            'town_or_city', 'country', 
        )
