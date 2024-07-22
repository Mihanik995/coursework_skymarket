from rest_framework import pagination, viewsets, generics

from ads.serializers import *


class AdPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 36


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = AdPagination

    def get_queryset(self):
        return Comment.objects.filter(ad=self.kwargs.get('ad_pk'))


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    def get_serializer_class(self):
        if self.action == "list":
            return AdSerializer
        else:
            return AdDetailSerializer


# class AdListAPIView(generics.ListAPIView):
#     queryset = Ad.objects.all()
#     serializer_class = AdSerializer
#
#
# class AdCreateAPIView(generics.CreateAPIView):
#     serializer_class = AdDetailSerializer


class MyAdListAPIView(generics.ListAPIView):
    serializer_class = AdSerializer

    def get_queryset(self):
        return Ad.objects.filter(self.request.user.pk)

# class AdRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Ad.objects.all()
#     serializer_class = AdDetailSerializer
#
#
# class AdUpdateAPIView(generics.UpdateAPIView):
#     queryset = Ad.objects.all()
#     serializer_class = AdDetailSerializer
#
#
# class AdDestroyAPIView(generics.DestroyAPIView):
#     queryset = Ad.objects.all()
