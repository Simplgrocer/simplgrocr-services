from langchain_google_genai import ChatGoogleGenerativeAI
from list_item_generator import ListItemGenerator


class GeminiListItemGenerator(ListItemGenerator):
    def __init__(self, prompt: str) -> None:
        llm = ChatGoogleGenerativeAI(model="gemini-pro")

        super().__init__(prompt, llm)

    def generate(self) -> str:
        base_response = self.generate_base_response

        return base_response
