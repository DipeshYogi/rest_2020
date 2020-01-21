from django.shortcuts import render
from . serializers import AddSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

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
