from rest_framework import serializers

def file_extn(name):
    extn = name.split(".")[-1]
    if extn not in ["jpg", "jpeg", "png"]:
        raise serializers.ValidationError("Please select an image")
    return name

class FaceplusAPISerializer(serializers.Serializer):
    path = serializers.CharField(required=True, max_length=500, validators=[file_extn])