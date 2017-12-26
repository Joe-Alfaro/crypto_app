from django.shortcuts import render

from .models import Condition
from rest_framework import viewsets
from .serializers import ConditionSerializer


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
