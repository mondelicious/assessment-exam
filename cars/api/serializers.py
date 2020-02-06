from rest_framework import serializers
from cars.models import Colors, Cars

from django.contrib.auth import get_user_model
User = get_user_model()


class CarsSerializer(serializers.ModelSerializer):
    color = serializers.SlugRelatedField(slug_field='name', queryset=Colors.objects.all(), allow_null=True, required=False)
    
    class Meta:
        model = Cars
        fields = "__all__"


class ColorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Colors
        fields = "__all__"
