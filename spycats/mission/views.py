from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from .models import Mission, Target
from .serializers import (
    MissionSerializer,
    AssignMissionSerializer,
    TargetUpdateSerializer,
    MissionDeleteSerializer
)


class MissionList(ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class MissionDetail(RetrieveAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class MissionDelete(DestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionDeleteSerializer

    def perform_destroy(self, instance):
        serializer = self.get_serializer(instance)
        serializer.validate({})
        instance.delete()


class AssignMission(UpdateAPIView):
    queryset = Mission.objects.all()
    serializer_class = AssignMissionSerializer


class TargetUpdate(UpdateAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetUpdateSerializer

