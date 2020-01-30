from django import forms
from .models import comment,Contatct

class commentForm(forms.ModelForm) :
    class Meta:
        model=comment
        fields=[
            'name',
            'email',
            'post_comment'
        ]
class ContatctForm(forms.ModelForm) :
    class Meta:
        model=Contatct
        fields=[
           'first_name',
            'last_name',
            'email',
            'message'
        ]

