import logging

from django.conf import settings
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import User

from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import get_object_or_404
from rest_condition import Not
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


logger = logging.getLogger(__name__)


class FakeLogin(generics.RetrieveAPIView):

    permission_classes = []

    def get(self, request, *args, **kwargs):
        '''
        username = request.query_params.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            return HttpResponse("User not found", status=404)
        '''
        user = authenticate(
            username=request.query_params.get('username'), 
            password=request.query_params.get('password')
        )
        print(user)
        if not user:
            return HttpResponse("Wrong password", status=404)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect('/')


class LogoutView(generics.DestroyAPIView):

    permission_classes = [IsAuthenticated, ]

    def delete(self, request, *args, **kwargs):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)

'''
class UserSelfView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserProfileSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_object(self):
        return self.request.user.userprofile
'''
