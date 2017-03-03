from django import forms
import requests


class OnboardForm(forms.Form):
    accept_coc = forms.BooleanField(label="I understand and agree to these conditions.")
    email = forms.EmailField(label="Your Email Address", help_text="We'll send your Slack invite here.")
    full_name = forms.CharField(required=False, label="Your Full Name", help_text="Optional")
