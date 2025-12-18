from rest_framework import serializers
from .models import AutomationJob

class AutomationJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutomationJob
        fields = '__all__'
        read_only_fields = ('status', 'created_at', 'result_file', 'report')
