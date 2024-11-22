from rest_framework import serializers
from cat.models import Cat
from .models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "name", "country", "description", "is_completed"]
        extra_kwargs = {"id": {"read_only": True}}


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)
    assigned_cat = serializers.SerializerMethodField()

    class Meta:
        model = Mission
        fields = ["id", "is_completed", "targets", "assigned_cat"]

    def get_assigned_cat(self, obj):
        cat = Cat.objects.filter(active_mission=obj).first()
        if cat:
            return {
                "id": cat.id,
                "name": cat.name,
                "breed": cat.breed,
                "years_of_experience": cat.years_of_experience,
                "salary": cat.salary,
            }
        return None

    def validate_targets(self, value):
        if not (1 <= len(value) <= 3):
            raise serializers.ValidationError(
                "A mission must have between 1 and 3 targets."
            )
        return value

    def create(self, validated_data):
        targets_data = validated_data.pop("targets")
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission


class AssignMissionSerializer(serializers.ModelSerializer):
    cat_id = serializers.PrimaryKeyRelatedField(
        queryset=Cat.objects.all(), source="assigned_cat"
    )

    class Meta:
        model = Mission
        fields = ["id", "cat_id"]

    def validate(self, data):
        cat = data["assigned_cat"]
        if cat.active_mission:
            raise serializers.ValidationError(
                f"{cat.name} already has an active mission."
            )

        if self.instance.is_completed:
            raise serializers.ValidationError("This mission is already completed.")

        return data

    def update(self, instance, validated_data):
        cat = validated_data["assigned_cat"]
        cat.active_mission = instance
        cat.save()
        return instance


class TargetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "description", "is_completed"]

    def validate(self, attrs):
        target = self.instance

        if target.mission.is_completed:
            raise serializers.ValidationError(
                "the mission is already completed."
            )

        if target.is_completed and 'description' in attrs:
            raise serializers.ValidationError(
                "a target that is already completed."
            )

        return attrs

    def update(self, instance, validated_data):
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.is_completed = validated_data.get(
            "is_completed", instance.is_completed
        )
        instance.save()

        mission = instance.mission
        if mission and not mission.is_completed:
            if not mission.targets.filter(is_completed=False).exists():
                mission.is_completed = True
                mission.save()
        return instance


class MissionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ['id']

    def validate(self, data):
        cat = Cat.objects.filter(active_mission=self.instance).first()
        if cat and not self.instance.is_completed:
            raise serializers.ValidationError(
                "This mission is assigned to a cat."
            )
        return data
