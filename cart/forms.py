from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(
    #     choices=PRODUCT_QUANTITY_CHOICES,
    #     coerce=int)
    quantity = forms.IntegerField(max_value=99,
                                  min_value=1)

    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
