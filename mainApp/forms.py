from django import forms
from .models import veiculo

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = veiculo
        fields = ["model_text", "placa_text", "status", "manutencao"]
        widgets = {
            'model_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Modelo do veículo'
            }),
            'placa_text': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Placa do veículo'
            }),
            'status':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Status do veículo'
            }),
            'manutencao':forms.DateInput(attrs={
                'class':'form-control',
                'type':'date'
            })
        }
        labels = {
            'model_text': 'Modelo',
            'placa_text': 'Placa',
            'status': 'Condição do veículo',
            'manutencao': 'Data de manutenção'
        }