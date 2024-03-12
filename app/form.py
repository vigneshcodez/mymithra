from django import forms
from .models import Messages


class MessagesForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Full Name", "class": "input-field"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Email", "class": "input-field"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Phone", "class": "input-field"}), label="")
    message = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Messages", "class": "input-field messageinput"}), label="")

    class Meta:
        model = Messages
        exclude = ("user",)
