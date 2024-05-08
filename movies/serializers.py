from django.db.models import Avg
from rest_framework import serializers

from actors.serializers import ActorSerializer
from awards.serializers import AwardSerializer
from genres.serializers import GenreSerializer
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lancamento não pode ser anterior a 1990.')
        return value


class MovieGatewaySerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    awards = AwardSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        # fields = "__all__"
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume', 'awards']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)

        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
