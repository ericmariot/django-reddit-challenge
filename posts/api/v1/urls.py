"""
API V1: Posts Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers
from topics.api.v1.urls import router as topic_router
from posts.api.v1.views import (
    PostViewSet,
)

###
# Routers
###
router = routers.NestedSimpleRouter(topic_router, r"topics", lookup="topic")
router.register(r"posts", PostViewSet, basename="topic-posts")

###
# URLs
###
urlpatterns = [
    url(r"^", include(router.urls)),
]
