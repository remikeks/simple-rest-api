from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=40, validators=[])

    class Meta:
        model = Person
        fields = '__all__'