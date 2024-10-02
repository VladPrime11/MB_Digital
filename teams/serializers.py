from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import re

from .models import Team, Person


class PersonSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=Person.objects.all())])
    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=50)

    def validate_first_name(self, value):
        if re.search(r'\d', value):
            raise serializers.ValidationError("The name must not contain numbers")
        return value

    def validate_last_name(self, value):
        if re.search(r'\d', value):
            raise serializers.ValidationError("Surname must not contain numbers")
        return value

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'team']


class TeamSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[UniqueValidator(queryset=Team.objects.all())])
    members = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']
