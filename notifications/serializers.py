from rest_framework import serializers
from . import models


class DeviceSerializer(serializers.Serializer):
    registration_id = serializers.CharField(max_length=256)


class DeviceUpdateSerializer(serializers.Serializer):
    old_token = serializers.CharField(max_length=256)
    new_token = serializers.CharField(max_length=256)


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = ('id', 'title', 'body', 'data', 'read', 'date',)