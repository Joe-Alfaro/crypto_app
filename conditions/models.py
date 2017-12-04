from django.db import models
from django.contrib.auth.models import User


class Condition(models.Model):
    user = models.ForeignKey(User, blank=False)


class ConditionType(models.Model):
    CONDITION_TYPES = (
        (1, 'relative_delta'),
        (2, 'absolute_delta'),
        )
    name = models.IntegerField(choices=CONDITION_TYPES)
