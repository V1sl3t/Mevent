from django.urls import path, include

from rest_framework import routers
from .viewsets import (
    ProfileViewSet,
    MyProfileViewSet,
    FollowerViewSet,
    UserRatingViewSet,
    ProfileEventViewSet,
    CityViewSet,
)

app_name = "profiles"
router = routers.SimpleRouter()

router.register('users/(?P<user_id>[^/.]+)/ratings', UserRatingViewSet, basename="UserRating")
router.register("users", ProfileViewSet, basename="Profiles")
router.register("users", FollowerViewSet, basename="Followers")
router.register("users", ProfileEventViewSet, basename="User events")
router.register("city", CityViewSet, basename="City")


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/me", MyProfileViewSet.as_view(), name="me"),
]
