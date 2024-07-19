from rest_framework import serializers
from .models import Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'course', 'student', 'midterm_grade', 'final_grade']

