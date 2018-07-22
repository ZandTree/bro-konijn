from django import forms
from django.core import validators
from .models import Blog

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    msg = forms.CharField(label="Your text",widget=forms.Textarea(attrs={'rows':10,'cols':80}))
    honey_pot = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)],label="empty")
    msg.widget.attrs.update({'class':'shape'})
    name.widget.attrs.update({'class':'shape'})
    email.widget.attrs.update({'class':'shape'})

class BlogForm(forms.ModelForm):
    honey_pot = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    class Meta:
        model = Blog
        fields = ["title","content"]
