from django.shortcuts import render
from rest_framework import viewsets, generics, parsers, permissions
from rest_framework.response import Response
from rest_framework.decorators import *
from .models import *
from .serializers import *


# Create your views here.

class RegulationViewSet(viewsets.ModelViewSet):
    queryset = Regulation.objects.filter(active=True)
    serializer_class = RegulationSerializer


class FalcutyViewSet(viewsets.ModelViewSet):
    queryset = Falcuty.objects.filter(active=True)
    serializer_class = FalcutySerializer


class ClassViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Class.objects.filter(active=True)
    serializer_class = ClassSerializer


class UserViewSet(viewsets.ViewSet,generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser, ]


    def get_permissions(self):
        if self.action in ['get_current_user']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get'], url_path='current-user', detail=False)
    def get_current_user(self, request):
        return Response(UserSerializer(request.user).data)


class ActivityViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Activity.objects.filter(active=True)
    serializer_class = ActivitySerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action.__eq__('list'):
            q = self.request.query_params.get('q')
            if q:
                queryset = queryset.filter(name__icontains=q)

            reg_id = self.request.query_params.get('regulation_id')
            if reg_id:
                queryset = queryset.filter(regulation_id=reg_id)

        return queryset


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.filter(active=True)
    serializer_class = PointSerializer