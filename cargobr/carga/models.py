from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Create your models here.

class Carga(models.Model):
    id = models.CharField(primary_key=True, max_length=6, editable=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dados = models.CharField(max_length=1000)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        insucess = True
        while insucess:
            temp_id = get_random_string(length=6)
            if not Carga.objects.filter(id=temp_id).exists() and not self.pk:
                self.id = temp_id
                insucess = False
        super(Carga, self).save(*args, **kwargs)

