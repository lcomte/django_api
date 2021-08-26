from django.conf.urls import url
from django_rest_api import views
urlpatterns = [
    url(r'^api/eurovalue', views.eurovalue),
    url(r'^api/webpage/data',views.webpageData)
]