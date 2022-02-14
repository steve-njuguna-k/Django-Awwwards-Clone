from rest_framework import serializers
from .models import Profile, Portfolio

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')
    first_name = serializers.ReadOnlyField(source='author.first_name')
    last_name = serializers.ReadOnlyField(source='author.last_name')
    email = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Profile
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')
    first_name = serializers.ReadOnlyField(source='author.first_name')
    last_name = serializers.ReadOnlyField(source='author.last_name')
    email = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Portfolio
        fields = '__all__'