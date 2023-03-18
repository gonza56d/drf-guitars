from rest_framework import serializers

from .models import Brand, Line


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Line
        fields = '__all__'
