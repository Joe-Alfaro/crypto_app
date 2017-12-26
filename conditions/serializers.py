from .models import Condition
from rest_framework import serializers


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ('id', )
