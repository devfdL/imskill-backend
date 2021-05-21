from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeacherSerializer
from .models import teacher
from rest_framework.response import Response
from rest_framework import permissions, status

# Create your views here.
class teacherView(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = teacher.objects.all()

    permission_classes = (permissions.AllowAny,)
    
