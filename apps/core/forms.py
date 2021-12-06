from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.TextInput(attrs={
                'class': 'input'
            })
        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
                'class': 'input'
            })