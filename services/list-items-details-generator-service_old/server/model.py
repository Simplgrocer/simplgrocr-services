from typing import List, Optional

from pydantic import BaseModel


class PromptSeriesSchema(BaseModel):
    """
    `PromptSeriesSchema` is a `BaseModel` with `prompts` fields
    """

    prompts: List[str]

    class Config:
        json_schema_extra = {"example": {"prompts": ["Fish 1kg 2/kg"]}}
