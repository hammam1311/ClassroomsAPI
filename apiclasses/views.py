from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from django.contrib.auth.models import User
from classes.models import Classroom
from .serializers import SignupSerializer,ClassroomSerializer,ClassroomSerializer,SignupSerializer,ClassroomDetailsSerializer,UpdateClassroomSerializer


class signup(CreateAPIView):
	serializer_class = SignupSerializer

class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer

class ClassroomDetails(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class UpdateClassroom(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UpdateClassroomSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class CreatClassroom(CreateAPIView):
	serializer_class = UpdateClassroomSerializer
	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)

class CancelClassroom(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'
