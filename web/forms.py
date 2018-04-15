from django import forms

class MessageForm(forms.Form):
        title = forms.CharField(max_length=50, required=True)
        subject = forms.CharField(max_length=1000, required=True)
