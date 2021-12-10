"""
API V1: Topics Views
"""
###
# Libraries
###
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from helpers.permissions import IsOwnerOrReadOnly

from topics.models import Topic
from topics.api.v1.serializers import (
    TopicRetrieveSerializer,
    TopicSerializer,
    TopicCreateUpdateDeleteSerializer,
)

###
# Filters
###


###
# Viewsets
###
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return TopicSerializer
        if self.action == "retrieve":
            return TopicRetrieveSerializer

        return TopicCreateUpdateDeleteSerializer

    lookup_field = "url_name"
