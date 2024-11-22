from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import CatSerializer, CatSalaryUpdateSerializer
from .models import Cat


class CatList(ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return CatSalaryUpdateSerializer
        else:
            return CatSerializer
