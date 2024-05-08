from django.utils import timezone

from rest_framework import serializers

from actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Actor
        fields = "__all__"

    def get_age(self, obj):
        today = timezone.now().date()
        age = int(
            today.year - obj.birthday.year - ((today.month, today.day) < (obj.birthday.month, obj.birthday.day))
        )

        if age:
            return age

        return None
