from dotenv import load_dotenv
import os

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(
    model="mistral-small-latest",   # ✅ updated name
    api_key=os.getenv("MISTRAL_API_KEY")
)



response = model.invoke("Why should I do after data analyst hsould i do domain specific or gen ai")
print(response.content)