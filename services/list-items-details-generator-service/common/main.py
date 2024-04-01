from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro")

result = llm.invoke(
    "Produce a raw JSON output without enclosing it in a markdown syntax. The json should contain these parameters: name, measurementUnit: which can be unit, kg or g depending on the input, quantity, and total price. Your input data is- Fish 1kg 2/kg"
)

print(result.content)
