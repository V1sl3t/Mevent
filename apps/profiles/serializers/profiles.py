from rest_framework import serializers

from apps.events.serializers import CategoryListSerializer
from apps.profiles.models import User
from apps.core.utils import delete_image_if_exists
from apps.profiles.utils import change_followers_if_exists


class ProfileRetrieveSerializer(serializers.ModelSerializer):
    category_favorite = CategoryListSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "city",
            "image_url",
            "is_email_verified",
            "is_private",
            "bio",
            "age",
            "category_favorite",
            "date_of_birth",
        )


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "image_url",
            "is_email_verified",
            "city",
            "is_private",
            "bio",
            "age",
            "category_favorite",
            "date_of_birth",
        )

    def update(self, instance, validated_data):
        if 'image_url' in validated_data and not validated_data['image_url']:
            delete_image_if_exists(instance)

        is_private = validated_data.get("is_private")
        if is_private is False:
            change_followers_if_exists(instance)

        return super().update(instance, validated_data)
