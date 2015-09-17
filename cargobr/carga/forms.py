from django import forms

from cargobr.carga.models import Carga


class CargaForm(forms.ModelForm):
    class Meta:
        model = Carga
        exclude = ['id']
