from ads.views import *
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

comment_router = routers.DefaultRouter()
comment_router.register('', CommentViewSet)

ad_router = routers.DefaultRouter()
ad_router.register('', AdViewSet)

urlpatterns = ad_router.urls + [
                  path('me/', MyAdListAPIView.as_view(), name='my_ads_list'),
                  path('<int:ad_pk>/comments/', include(comment_router.urls))
              ]
