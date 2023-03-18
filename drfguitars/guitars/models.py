from django.db import models

from drfguitars.utils.models import NamedModel


class Guitar(NamedModel):

    line = models.ForeignKey('brands.Line', on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
