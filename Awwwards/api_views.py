from django.contrib.auth.decorators import login_required
from rest_framework import generics
from django.shortcuts import render
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from .serializers import PortfolioSerializer, ProfileSerializer
from .models import Portfolio, Profile

class PortfolioAPI(generics.ListCreateAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated ]

    def get_queryset(self):
        """
        This view should return a list of all the properties
        created by the currently authenticated user.
        """
        user = self.request.user
        return Portfolio.objects.filter(author=user)

    def perform_create(self, serializer):
        """
        This view should create a new property listing
        for the currently authenticated user.
        """
        serializer.save(author=self.request.user)

class PortfolioDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated , IsOwnerOrReadOnly]

class ProfileAPI(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated ]

    def get_queryset(self):
        """
        This view should return a list of all the properties
        created by the currently authenticated user.
        """
        user = self.request.user.id
        return Profile.objects.filter(author=user)

    def perform_create(self, serializer):
        """
        This view should create a new property listing
        for the currently authenticated user.
        """
        serializer.save(author=self.request.user)

class ProfileDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated , IsOwnerOrReadOnly]