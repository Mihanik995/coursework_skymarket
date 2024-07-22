from django.urls import path, include
from rest_framework import routers

from ads.views import *

comment_router = routers.DefaultRouter()
comment_router.register(r'comments', CommentViewSet)

ad_router = routers.DefaultRouter()
ad_router.register('', AdViewSet)

urlpatterns = [
                  # path('', AdListAPIView.as_view(), name='ads_list'),
                  # path('', AdCreateAPIView.as_view(), name='new_add'),
                  path('me/', MyAdListAPIView.as_view(), name='my_ads_list'),
                  # path('<int:pk>/', AdRetrieveAPIView.as_view(), name='add_detail'),
                  # path('<int:pk>/', AdUpdateAPIView.as_view(), name='edit_add'),
                  # path('<int:pk>/', AdDestroyAPIView.as_view(), name='delete_add'),
                  path('<int:ad_pk>/', include(comment_router.urls))
              ] + ad_router.urls
