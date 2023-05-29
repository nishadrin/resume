from rest_framework import generics
from rest_framework.exceptions import MethodNotAllowed
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

from resumeapp.models import Resume
from resumeapp.permissons import ResumePermission
from resumeapp.serializers import ResumeSerializer

User = get_user_model()


class ResumeView(generics.RetrieveUpdateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [ResumePermission]

    @swagger_auto_schema(auto_schema=None)
    def put(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)
