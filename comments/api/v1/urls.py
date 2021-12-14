"""
API V1: Comments Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers
from posts.api.v1.urls import router as post_router
from comments.api.v1.views import (
    CommentViewSet,
)

###
# Routers
###
router = routers.NestedSimpleRouter(post_router, r"posts", lookup="post")
router.register(r"comments", CommentViewSet, basename="post-comments")

###
# URLs
###
urlpatterns = [
    url(r"^", include(router.urls)),
]
