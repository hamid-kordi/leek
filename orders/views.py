from django.shortcuts import render
from .serializers import OrderItemSerializer, ReportSerializer, OrdersSerializer
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOrderUser
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .models import OrderItem, Orders, Report
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


class OrderManageView(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrderItemManageView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class ReportManageView(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


# class OrderManageView(viewsets.ViewSet):
#     query_set = Orders.objects.all()
#     serializer_class = OrdersSerializer

#     def list(self, request):
#         """
#         for get all orders
#         """
#         srz_ordrs = OrdersSerializer(instance=self.query_set, many=True)
#         return Response(data=srz_ordrs.data, status=status.HTTP_200_OK)

#     def retrieve(self, request, pk=None):
#         order = get_object_or_404(self.query_set, pk=pk)
#         # self.check_object_permissions(request,)
#         srz_ordrs = OrdersSerializer(instance=order)
#         return Response(data=srz_ordrs.data, status=status.HTTP_200_OK)

#     # @action(
#     #     detail=True,
#     #     methods=["post"],
#     #     permission_classes=[IsAuthenticated,IsOrderUser],
#     # )
#     def create(self, request):
#         srz_data = OrdersSerializer(instance=request.data)
#         if srz_data.is_valid():
#             srz_data.create(srz_data.validated_data)
#             return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
#         return Response(srz_data.errors, status=status.HTTP_201_CREATED)

#     def partial_update(self, request, pk=None):

#         pass

#     def destroy(self, request, pk=None):
#         pass


# class OrderItemManageView(viewsets.ViewSet):
#     query_set = Orders.objects.all()

#     def list(self, request):
#         """
#         for get all orders
#         """
#         srz_ordrs = OrdersSerializer(instance=self.query_set, many=True)
#         return Response(data=srz_ordrs.data, status=status.HTTP_200_OK)

#     def retrieve(self, request, pk=None):
#         order = get_object_or_404(self.query_set, pk=pk)
#         # self.check_object_permissions(request,)
#         srz_ordrs = OrdersSerializer(instance=order)
#         return Response(data=srz_ordrs.data, status=status.HTTP_200_OK)

#     # @action(
#     #     detail=True,
#     #     methods=["post"],
#     #     permission_classes=[IsAuthenticated,IsOrderUser],
#     # )
#     def create(self, request):
#         srz_data = OrdersSerializer(instance=request.data)
#         if srz_data.is_valid():
#             srz_data.create(srz_data.validated_data)
#             return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
#         return Response(srz_data.errors, status=status.HTTP_201_CREATED)

#     def partial_update(self, request, pk=None):

#         pass

#     def destroy(self, request, pk=None):
#         pass


# class ReportManageView(viewsets.ViewSet):
#     query_set = Orders.objects.all()

#     def list(self, request):
#         """
#         for get all orders
#         """
#         srz_ordrs = OrdersSerializer(instance=self.query_set, many=True)
#         return Response(data=srz_ordrs.data, status=status.HTTP_200_OK)

#     def retrieve(self, request, pk=None):
#         order = get_object_or_404(self.query_set, pk=pk)
#         # self.check_object_permissions(request,)
#         srz_ordrs = OrdersSerializer(instance=order)
#         return Response(data=srz_ordrs.data, status=status.HTTP_200_OK)

#     # @action(
#     #     detail=True,
#     #     methods=["post"],
#     #     permission_classes=[IsAuthenticated,IsOrderUser],
#     # )
#     def create(self, request):
#         srz_data = OrdersSerializer(instance=request.data)
#         if srz_data.is_valid():
#             srz_data.create(srz_data.validated_data)
#             return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
#         return Response(srz_data.errors, status=status.HTTP_201_CREATED)

#     def partial_update(self, request, pk=None):

#         pass

#     def destroy(self, request, pk=None):
#         pass
