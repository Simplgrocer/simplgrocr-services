import json
import logging
import sys

from typing import Dict

from langchain_google_genai import ChatGoogleGenerativeAI

from fastapi import APIRouter, Body, HTTPException, Request

from server.model import PromptSeriesSchema

from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro")

list_items_details_generator_router = APIRouter()


@list_items_details_generator_router.post(
    path="/", summary="Generate details for the list items"
)
async def generate_list_items_details(
    request: Request, prompt_series: PromptSeriesSchema = Body(...)
) -> Dict:
    """
    "Generate details for the list items"

    The function is a POST request, and it takes in a JSON body

    :param request:
    :param prompts: PromptSeriesSchema = Body(...)
    :type prompt_series: PromptSeriesSchema
    :return: A dictionary with a message key and a value of the message returned from the enquiry
    submitter.
    """
    body = prompt_series.model_dump()

    print(body)

    result = llm.invoke(
        "Produce a raw JSON output without enclosing it in a markdown syntax. The json should contain these parameters: name, measurementUnit: which can be unit, kg or g depending on the input, quantity, and total price. Your input data is- Fish 1kg 2/kg"
    )

    print(result.content)

    return json.loads(result.content)
