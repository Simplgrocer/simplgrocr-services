import json
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ListItemSerializer, PromptSerializer

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro")


@api_view(["POST"])
def generate_list_items(request):
    if not request.data:
        return Response({"error": "Request body is required."}, status=400)

    serializer = PromptSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    prompts_data = serializer.validated_data.get("prompts")

    prompts_list = prompts_data.split("\n")

    result = llm.invoke(f'Transform a list of items {prompts_list} described in strings into a structured array of objects. Each item string, such as "Chips 1 unit 10/unit", will be converted into an object with specific attributes: "name", "unitOfMeasurement", "quantity", "pricePerUnitOfMeasurement", and "totalPrice". The "name" attribute will identify the item (e.g., "Chips"), the "unitOfMeasurement" will specify the measurement unit (e.g., "unit", "kg", or "g"), the "quantity" will note the amount, and the "pricePerUnitOfMeasurement" will detail the cost per unit of measurement. Finally, calculate the "totalPrice" based on the unit of measurement and the price per unit. For units measured in "unit", the total price should be the product of quantity and price per unit. For items measured in "kg" or "g", the total price calculation will adjust accordingly. Use the provided array of strings as your input and generate the corresponding array of objects as the output. Just produce the raw JSON without any wrappings as the output.')

    print(result)

    return Response(json.loads(result.content), status=200)
