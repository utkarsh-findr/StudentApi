from rest_framework import serializers
from api import models

class InstititeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Institute
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    institite=InstititeSerializer(read_only=True)
    class Meta:
        model=models.Student
        fields='__all__'