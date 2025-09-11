import datetime

from django.db import models
from django.utils import timezone

class veiculo(models.Model):
    model_text = models.CharField(max_length=200, verbose_name="Modelo:")
    placa_text = models.CharField(max_length=7, verbose_name="Placa:")
    status = models.CharField(verbose_name="Status:", on_delete=models.CASCADE)
    manutencao = models.DateField(verbose_name="Data de Manutenção: ")
    def publicado_recentemente(self):
        return self.manutencao >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.model_text