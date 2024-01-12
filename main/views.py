import datetime

from django.http import Http404
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Habits
from main.pagination import MyPagination
from main.serializers import HabitsSerializer


class ChecksUser:
    def get_object(self):
        self.object = super().get_object()
        if self.object.user != self.request.user and not self.object.sing_publicity:
            raise Http404
        return self.object


class Logout(APIView):

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        now = timezone.now()
        serializer.save()
        self.request.user.habits_set.add(serializer.instance)
        serializer.instance.data_next_reminder = now
        if serializer.instance.perform_time.hour < now.hour:
            serializer.instance.data_next_reminder = serializer.instance.data_next_reminder + datetime.timedelta(days=1)
        serializer.instance.save()


class HabitsUpdateAPIView(ChecksUser, generics.UpdateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated]


class HabitsDestroyAPIView(ChecksUser, generics.DestroyAPIView):
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated]


class HabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class HabitsListPublicityAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.filter(sing_publicity=True)
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination
