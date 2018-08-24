from django import forms


class OtpPhoneNumberForm(forms.Form):
    phone = forms.IntegerField()