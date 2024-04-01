from rest_framework import serializers


class PromptSerializer(serializers.Serializer):
    prompts = serializers.CharField()
