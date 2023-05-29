from rest_framework import serializers

from resumeapp.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        exclude = ['created_at', 'updated_at', 'id', 'is_active', 'user', ]
