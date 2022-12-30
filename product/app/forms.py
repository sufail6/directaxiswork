from django import forms

from app.models import product


class items(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'