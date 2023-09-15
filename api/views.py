from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

# Create your views here.
class PersonCreateView(generics.CreateAPIView):
    serializer_class = PersonSerializer

class PersonRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    lookup_field = 'user_id'

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Person.objects.filter(user_id=user_id)