from django.conf.urls import url

from histogram_app.views import HistogramView, get_histogram

urlpatterns = [
    # url(r'^$', HistogramView.as_view(), name='histogram_app_main'),
    url(r'^$', get_histogram, name='histogram_app_main'),
]
