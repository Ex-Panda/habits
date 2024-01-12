from rest_framework import serializers

from main.models import Habits
from main.validators import AwardValidator, TimeCompletedValidator, RelatedValidator, PleasureHabitsValidator


class HabitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habits
        exclude = ['user']
        validators = [AwardValidator(field1='related_habit', field2='award'), TimeCompletedValidator(field='time_completed'), RelatedValidator(field='related_habit'), PleasureHabitsValidator(field='related_habit'),]
