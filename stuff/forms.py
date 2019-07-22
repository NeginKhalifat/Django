from django import forms
from . import models

class CreateStuff(forms.ModelForm):
    class Meta:
         model = models.stuff
         fields = ['name','price','slug','picture','markdown','commutative']