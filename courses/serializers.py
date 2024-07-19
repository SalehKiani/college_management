from rest_framework import serializers
from .models import Course, Attendance


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'professor', 'students', 'units']


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'course', 'student', 'date', 'is_present']
