from dotenv import load_dotenv


load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(
    model="mistral-small-latest",  
)

print("chosse your AI mode")
print("press 1 for Angry mode")
print("press 2 for funny mode ")
print("press 3 for sad mode")

choice = int(input("tell your response :- "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."
else:
    print("Invalid choice! Defaulting to normal mode.")  # ✅ handles invalid input
    mode = "You are a helpful AI assistant."

messages = [
    SystemMessage(content=mode)

]


print("-------------Welcome type 0 to exist the application--------------")
while True:
    
    prompt = input("you:")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot:",response.content)



print(messages)