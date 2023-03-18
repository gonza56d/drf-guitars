from rest_framework import viewsets

from .models import Guitar
from .serializers import GuitarSerializer


class GuitarViewSet(viewsets.ModelViewSet):

    queryset = Guitar.objects.filter(hidden=False)
    serializer_class = GuitarSerializer
