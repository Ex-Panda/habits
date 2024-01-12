from rest_framework.serializers import ValidationError


class AwardValidator:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit_value = dict(value).get(self.field1)
        award_value = dict(value).get(self.field2)

        if related_habit_value is not None and award_value is not None:
            raise ValidationError('Запрещен одновременный выбор связанной привычки и указания вознаграждения.')


class TimeCompletedValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_completed_value = dict(value).get(self.field)
        if time_completed_value is not None:
            if time_completed_value > 120:
                raise ValidationError('Время выполнения должно быть не больше 120 секунд.')


class RelatedValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        habits_value = dict(value).get(self.field)
        if habits_value is not None:
            if not habits_value.sing_pleasure:
                raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')


class PleasureHabitsValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        habits_value = dict(value).get(self.field)
        if habits_value is not None:
            if habits_value.sing_pleasure and habits_value.award is not None and habits_value.related_habit is not None:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')
