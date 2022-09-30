from django.shortcuts import render

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order

from .serializers import OrderSerializer, MyOrderSerializer


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    s = OrderSerializer(data=request.data)
    if s.is_valid():
        try:
            s.save(user=request.user)
            return Response(s.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    
    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_order(request):
    order = Order.objects.filter(user=request.user)
    s = MyOrderSerializer(order, many=True)
    return Response(s.data)
