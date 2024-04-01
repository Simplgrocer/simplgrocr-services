from rest_framework import serializers


class PromptSerializer(serializers.Serializer):
    prompts = serializers.CharField()


class ListItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    measurementUnit = serializers.ChoiceField(choices=('unit', 'kg', 'g'))
    quantity = serializers.FloatField()
    totalPrice = serializers.FloatField()
