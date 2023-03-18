from rest_framework import viewsets

from .models import Brand, Line
from .serializers import BrandSerializer, LineSerializer


class BrandViewSet(viewsets.ModelViewSet):

    queryset = Brand.objects.filter(hidden=False)
    serializer_class = BrandSerializer


class LineViewSet(viewsets.ModelViewSet):

    queryset = Line.objects.filter(hidden=False)
    serializer_class = LineSerializer

    def list(self, request, brand_id: int, *args, **kwargs):
        self.queryset = Line.objects.filter(hidden=False, brand__id=brand_id)
        return super().list(request, brand_id, *args, **kwargs)
