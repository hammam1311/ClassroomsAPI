from rest_framework import serializers
from classes.models import Classroom, Student
from django.contrib.auth.models import User

class ClassroomListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['name', 'subject', 'year', 'teacher']


class ClassroomDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'


class ClassroomCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'name', 'year']

class ClassroomUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'name', 'year']