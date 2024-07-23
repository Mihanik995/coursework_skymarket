from ads.permissions import *
from ads.serializers import *
from rest_framework import pagination, viewsets, generics
from rest_framework.permissions import IsAuthenticated


class AdPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 36


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = AdPagination

    def get_permissions(self):
        if self.action in ['list', 'create']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['partial_update', 'update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAdmin | IsOwner]
        return [permission() for permission in self.permission_classes]

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

    def get_permissions(self):
        if self.action in ['retrieve', 'create']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['partial_update', 'update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAdmin | IsOwner]
        return [permission() for permission in self.permission_classes]


class MyAdListAPIView(generics.ListAPIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ad.objects.filter(self.request.user.pk)
