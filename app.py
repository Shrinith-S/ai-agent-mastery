from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

print("=== AI Agent Mastery ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = client.responses.create(
        model="gpt-5-mini",
        input=user_input
    )

    print(f"AI: {response.output_text}\n")