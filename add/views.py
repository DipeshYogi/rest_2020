from django.shortcuts import render
from . serializers import AddSerializer, ItemsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from add import models

class AddApiView(APIView):
    serializer_class = AddSerializer

    def post(self,request):
        """Add two numbers"""
        ser = self.serializer_class(data = request.data)
        if ser.is_valid():
            n1 = ser.validated_data.get('n1')
            n2 = ser.validated_data.get('n2')
            n3 = n1 + n2

            return Response({f'The sum of {n1} & {n2} is':n3})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateItemView(APIView):
    serializer_class = ItemsSerializer

    def post(self,request):
        ser = self.serializer_class(data = request.data)
        if ser.is_valid():
            itm = models.Items.objects.create(
                                            name = ser.validated_data['name'],
                                            price = ser.validated_data['price'],
                                            exp_date = ser.validated_data['exp_date']
                            )
            return Response({'Item created successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
