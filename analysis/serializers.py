from rest_framework import serializers
from analysis.models import StockName, StockPrices
from datetime import datetime


class StockPricesSerializer(serializers.ModelSerializer):
    percentage = serializers.SerializerMethodField()
    stock_date = serializers.DateTimeField(format='%b %d, %Y')

    def get_percentage(self, obj):
        percentage_value = ((obj.stock_close - obj.stock_open)/obj.stock_close)*100
        return round(percentage_value,2)

    class Meta:
        model = StockPrices
        fields = ('stock_date', 'stock_open', 'stock_close','percentage')


class StockNameSerializer(serializers.ModelSerializer):
    stocks = StockPricesSerializer(many=True,read_only=True)

    class Meta:
        model = StockName
        fields = ('name','stocks',)


class TopStockPricesSerializer(serializers.ModelSerializer):
    stock_date = serializers.DateTimeField(format='%b %d, %Y')

    class Meta:
        model = StockPrices
        fields = ('stock_date', 'stock_volume')


class TopStockNameSerializer(serializers.ModelSerializer):
    top_stocks = serializers.SerializerMethodField()

    def get_top_stocks(self, stock):
        query_set = StockPrices.objects.filter( stock_id=stock).order_by('-stock_volume')[:5]
        serializer = TopStockPricesSerializer(instance=query_set, many=True)
        return serializer.data

    class Meta:
        model = StockName
        fields = ('name','top_stocks',)



 