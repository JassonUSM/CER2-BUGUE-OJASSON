from django import forms
from .models import LugarPatrimonial

class LugarPatrimonialForm(forms.ModelForm):
    class Meta:
        model = LugarPatrimonial
        fields = ['nombre', 'descripcion', 'imagen', 'ubicacion', 'anioConstruccion', 'categoria']