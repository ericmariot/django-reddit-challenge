"""
API V1: Posts Views
"""
###
# Libraries
###
from rest_framework import viewsets
from helpers.permissions import IsAuthorOrReadOnly
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action

from topics.models import Topic
from posts.models import Post
from posts.api.v1.serializers import (
    PostSerializer,
    PostRetrieveSerializer,
    PostCreateUpdateDeleteSerializer,
)

###
# Filters
###


###
# Viewsets
###
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        topic = Topic.objects.get(url_name=self.kwargs["topic_url_name"])
        return Post.objects.with_votes().filter(topic=topic.id)

    def perform_create(self, serializer):
        topic = Topic.objects.get(url_name=self.kwargs["topic_url_name"])
        serializer.save(author=self.request.user, topic=topic)

    def get_serializer_class(self):
        if self.action == "list":
            return PostSerializer
        if self.action == "retrieve":
            return PostRetrieveSerializer

        return PostCreateUpdateDeleteSerializer

    @action(detail=True, url_path="upvote", methods=["post"])
    def upvote(self, request, pk=None, topic_url_name="topic_url_name"):
        post = get_object_or_404(Post, pk=pk)
        post.vote = Post.Vote.UPVOTED
        post.save()

        return Response()
