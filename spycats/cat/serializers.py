from rest_framework import serializers
from validation.validate_breed import check_breed
from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ["id", "name", "years_of_experience", "breed", "salary"]

    def validate_years_of_experience(self, attr):
        if attr < 0:
            raise serializers.ValidationError(
                f"Years_of_experience '{attr}' is not valid."
            )
        return attr

    def validate_salary(self, attr):
        if attr < 0:
            raise serializers.ValidationError(f"Salary '{attr}' is not valid.")
        return attr

    def validate_breed(self, attr):
        if not check_breed(attr):
            raise serializers.ValidationError(f"Breed '{attr}' is not valid.")
        return attr


class CatSalaryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['salary']

    def validate_salary(self, attr):
        if attr < 0:
            raise serializers.ValidationError(f"Salary '{attr}' is not valid.")
        return attr
