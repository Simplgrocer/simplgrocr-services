from abc import ABC, abstractmethod


class LLMTextGenerator(ABC):
    def __init__(self, prompt: str, llm) -> None:
        self.prompt = prompt
        self.llm = llm

    @abstractmethod
    def generate_base_response(self) -> str:
        self.llm.invoke
