from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'}), 
        max_length=100
        )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'}),
        max_length=200
        )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}),
        max_length=5000
        )