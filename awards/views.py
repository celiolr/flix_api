from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultPermission
from awards.models import Award
from awards.serializers import AwardSerializer


# Create your views here.
class AwardCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Award.objects.all()
    serializer_class = AwardSerializer


class AwardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
