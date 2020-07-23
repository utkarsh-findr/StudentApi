from rest_framework.response import Response
from api import models, serializers
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)

class StudentListView (ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer

class StudentsDetailView(RetrieveUpdateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer

class InstituteListView (ListAPIView):
    queryset=models.Institute.objects.all()
    serializer_class=serializers.InstititeSerializer