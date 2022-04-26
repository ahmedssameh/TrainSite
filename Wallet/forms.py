from django import forms
from .models import UserWallet


class WalletUpdateForm(forms.ModelForm):
    class Meta:
        model = UserWallet
        fields = "__all__"
