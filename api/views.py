from django.shortcuts import render
from .serializers import ChemicalSerializer,ChemCompoSerializer, CommoditySerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Chemical, ChemCompo, Commodity
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
# Create your views here.

class CommodityViewSet(ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticated]


class ChemicalViewSet(ModelViewSet):
    queryset = Chemical.objects.all()
    serializer_class = ChemicalSerializer
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly]

class ChemCompViewSet(ModelViewSet):
    queryset = ChemCompo.objects.all()
    serializer_class = ChemCompoSerializer
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly]