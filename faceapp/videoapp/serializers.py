from rest_framework import serializers

class FaceplusAPISerializer(serializers.Serializer):
    path = serializers.CharField(required=True, max_length=500)