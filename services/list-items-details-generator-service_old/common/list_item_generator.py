from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from llm_text_generator import LLMTextGenerator

load_dotenv()

class ListItemGenerator(LLMTextGenerator):
    def __init__(self, prompt: str, llm) -> None:
        super().__init__(prompt, llm)

    def generate_base_response(self) -> str:
        return self.llm.invoke(self.prompt)
