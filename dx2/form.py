from django import forms

from dx2.models import board


class PostForm(forms.ModelForm):
    class Meta:
        model = board
        fields = ('title','contents',)


