from datetime import date, datetime

from django.utils import timezone

from rest_framework import serializers

from actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Actor
        fields = "__all__"

    # def get_age(self, obj):
    #     today = timezone.now().date()
    #     age = int(
    #         today.year - obj.birthday.year - ((today.month, today.day) < (obj.birthday.month, obj.birthday.day))
    #     )
    #
    #     if age:
    #         return age
    #
    #     return None

    # Function by ChatGPT
    def get_age(self, obj):
        today_now = datetime.now()
        actual_year = today_now.year
        actual_month = today_now.month
        actual_day = today_now.day

        birthday_year = obj.birthday.year
        birthday_month = obj.birthday.month
        birthday_day = obj.birthday.day

        age = actual_year - birthday_year

        if actual_month < birthday_month or (actual_month == birthday_month and actual_day < birthday_day):
            age -= 1

        if age >= 0:
            return age

        return None
