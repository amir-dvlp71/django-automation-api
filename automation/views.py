from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import AutomationJob
from .serializers import AutomationJobSerializer
from .services import process_file

class AutomationJobViewSet(viewsets.ModelViewSet):
    queryset = AutomationJob.objects.all()
    serializer_class = AutomationJobSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        job = serializer.save()
        process_file(job)  
