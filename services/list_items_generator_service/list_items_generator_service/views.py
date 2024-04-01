from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PromptSerializer


@api_view(["POST"])
def generate_list_items(request):
    if not request.data:
        return Response({"error": "Request body is required."}, status=400)

    serializer = PromptSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    prompts_data = serializer.validated_data.get("prompts")

    prompts_list = prompts_data.split("\n")

    print(prompts_list)

    return Response({"message": "Request received successfully."}, status=200)
