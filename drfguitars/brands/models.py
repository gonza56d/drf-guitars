from django.db import models

from drfguitars.utils.models import NamedModel


class Brand(NamedModel):

    pass


class Line(NamedModel):

    brand = models.ForeignKey('brands.Brand', on_delete=models.CASCADE)
