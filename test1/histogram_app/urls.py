from django.conf.urls import url

from histogram_app.views import HistogramView, HistogramResultView #, get_histogram

urlpatterns = [
    url(r'^$', HistogramView.as_view(), name='histogram_app_main'),
    url(r'^result/$', HistogramResultView.as_view(), name='histogram_app_result'),
    # url(r'^$', get_histogram, name='histogram_app_main'),
]
