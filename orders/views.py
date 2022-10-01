from locale import currency
import stripe
from django.conf import settings
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
        stripe.api_key = settings.STRIPE_SECRET_KEY
        total_price_stripe = int(s.validated_data.get('total_price'))
        print(total_price_stripe)
        try:
            charge = stripe.Charge.create(
                amount = total_price_stripe * 100,
                currency = 'USD',
                description = "Charge for Geek's Store",
                source = s.validated_data.get('stripe_token')
            )
            print('success')
            s.save(user=request.user)
            return Response(s.data, status=status.HTTP_201_CREATED)
        except Exception:
            print('failed')
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    
    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_order(request):
    order = Order.objects.filter(user=request.user)
    s = MyOrderSerializer(order, many=True)
    return Response(s.data)
