from django import forms

class Message_Form(forms.Form):
    to = forms.CharField(max_length=100)
    message = forms.CharField(max_length=100)
    