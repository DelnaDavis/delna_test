# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from analysis.models import StockName, StockPrices
from analysis.serializers import StockNameSerializer, TopStockNameSerializer



class StockLIstView(APIView):
	def get(self, request, format=None):
		stock_list = StockName.objects.all()
		serializer = StockNameSerializer(stock_list,many=True)
		return Response({"Stock":serializer.data}, status=status.HTTP_200_OK)


class TopStocksView(APIView):
	def get(self, request, format=None):
		stock_list = StockName.objects.all()
		serializer = TopStockNameSerializer(stock_list,many=True)
		return Response({"Stock":serializer.data}, status=status.HTTP_200_OK)