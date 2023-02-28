from django import forms


class AddToCardProductForm(forms.Form):
    QUANTITY_CHOISES = [(i, str(i)) for i in range(1, 30)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOISES, coerce=int)
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
