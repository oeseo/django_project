from rest_framework import serializers
from .models import CustomUser, Position

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'full_name', 'position', 'dismissed', 'dismissal_date']
