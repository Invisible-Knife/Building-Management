from django.shortcuts import render
from rest_framework import generics
from .serializers import HumanSerializer
from .models import Human

# Create your views here.


class HumanView(generics.ListAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer