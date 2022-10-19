from rest_framework import serializers
from apps.main import models


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Platform
        fields = [
            "name",
            "status",
            "logo",
        ]


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technology
        fields = [
            "name",
            "types",
            "language",
            "logo",
        ]
