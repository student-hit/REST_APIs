from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
class ProductView(APIView):
     def get(self, request, pk=None):
          if pk:
               product = Product.objects.get(id=pk)
               serializer = ProductSerializer(product)
               return Response({"status": "Request Successful", "data": serializer.data}, status=status.HTTP_200_OK)

          product = Product.objects.all()
          serializer = ProductSerializer(product, many=True)
          return Response({"status": "Request Successful", "data": serializer.data}, status=status.HTTP_200_OK)

     def post(self, request, *args, **kwargs):
          serializer = ProductSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response({"status": "Request Successful", "data": serializer.data}, status=status.HTTP_200_OK)
          else:
               return Response({"status": "An error", "details": serializer.error}, status=status.HTTP_400_BAD_REQUEST)

     def patch(self, request, pk=None, *args, **kwargs):
          product = Product.objects.get(id=pk)
          serializer = ProductSerializer(instance=product, data=request.data, partial=True)

          if serializer.is_valid():
               serializer.save()
               return Response({"status": "Request Successful", "data": serializer.data}, status=status.HTTP_200_OK)
          else:
               return Response({"status": "An error", "details": serializer.error}, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, pk=None):
          product = get_object_or_404(Product, id=pk)
          product.delete()
          return Response({"status": "success", "data": "Item deleted"})

          