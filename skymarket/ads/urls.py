from django.urls import path, include
from rest_framework import routers

from ads.views import *

comment_router = routers.DefaultRouter()
comment_router.register(r'comments', CommentViewSet)

ad_router = routers.DefaultRouter()
ad_router.register('', AdViewSet)

urlpatterns = ad_router.urls + [
                  path('me/', MyAdListAPIView.as_view(), name='my_ads_list'),
                  path('<int:ad_pk>/', include(comment_router.urls))
              ]
