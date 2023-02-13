

from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'first_name': _('Enter First Name'),
            'last_name': _('Enter Last Name'),
            'email': _('Email')
        }


# Raise exception if user inputs , in fields


# def validate_comma(value):
#     if "," in value:
#         raise forms.ValidationError("Invalid")
#     return value


# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=100, required=False, label="Enter First Name", help_text="Enter characters only")
#     last_name = forms.CharField(max_length=100, validators=[validate_comma])
#     email = forms.EmailField(max_length=100)

# def clean_first_name(self):
#     data = self.cleaned_data['first_name']
#     if "," in data:
#         raise forms.ValidationError("Invalid First Name")
#     return data
