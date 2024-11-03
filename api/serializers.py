from rest_framework import serializers
from .models import Petition, Vote

class PetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petition
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'petition']
        read_only_fields = ['user']  # Ensure user is assigned automatically

