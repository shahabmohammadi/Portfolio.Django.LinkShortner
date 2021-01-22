from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(label='', widget=forms.TextInput(attrs={'placeholder': "Your link goes here"}))
