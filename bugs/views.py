from rest_framework.viewsets import ModelViewSet
from .models import Bug
from .serializers import BugSerializer

class BugViewSet(ModelViewSet):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer