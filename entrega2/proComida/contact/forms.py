from django import forms

class ContactForm(forms.Form):
    name = forms.forms.CharField(label="Nombre", min_lenght=3, max_length=50, required=True)
    email = forms.forms.EmailField(label="Email", min_lenght=3, max_length=100, required=False)
    message = forms.forms.CharField(label="Mensaje",min_lenght=3, max_length=300, required=True)