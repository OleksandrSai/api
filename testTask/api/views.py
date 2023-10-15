from django.shortcuts import render
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Counter
from .serializer import CounterSerializer


# Create your views here.

class CounterViews(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   GenericViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer

    def update(self, request, *args, **kwargs):
        try:
            serial_num = kwargs.get("pk")
            instance = Counter.objects.get(serial_number=serial_num)
            serializer = CounterSerializer(data=request.data, instance=instance, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except:
            return Response({"Error":"Сan't find the serial number"})