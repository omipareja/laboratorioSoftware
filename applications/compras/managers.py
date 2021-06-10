from django.db import models
from django.db.models import Q, Sum, F, FloatField, ExpressionWrapper

class CarroComprasManager(models.Manager):

    def total_cobrar(self,pk):

        consulta = self.filter(user=pk).aggregate(
            total = Sum (
                F('cantidad')*F('productos__precio'),
                output_field= FloatField()
            ),
        )

        if consulta['total']:
            return consulta['total']
        else:
            return 0


class ReservasManager(models.Manager):

    def total_cobrar_reservas(self,pk):

        consulta = self.filter(user=pk).aggregate(
            total = Sum (
                F('cantidad')*F('productos__precio'),
                output_field= FloatField()
            ),
        )

        if consulta['total']:
            return consulta['total']
        else:
            return 0