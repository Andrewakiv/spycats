from rest_framework import serializers
from validation.validate_breed import check_breed
from models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ["name", "years_of_experience", "breed", "salary"]

    def validate_breed(self, attr):
        if not check_breed(attr):
            raise serializers.ValidationError(f"Breed '{attr}' is not valid.")
        return attr
