from django.conf.urls import url, include

from analysis.views import StockLIstView,TopStocksView

urlpatterns = [

    url(r'^stock-list/$', StockLIstView.as_view()),
    url(r'^top-stocks/$', TopStocksView.as_view()),

]