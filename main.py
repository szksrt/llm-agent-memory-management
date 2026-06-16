import os

from dotenv import load_dotenv
from google import genai
from memory import Memory

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

history = []

memory = Memory()

while True:
    user_input = input("You > ")

    if user_input == "exit":
        break
    
    memory.add(user_input)

    print("\n===== LONG TERM MEMORY =====")
    print(memory.get_all())
    print("============================\n")

    retrieved_memory = memory.retrieve(
        user_input
    )

    print("\n===== RETRIEVED MEMORY =====")
    print(retrieved_memory)
    print("============================\n")

    history.append(
        f"User: {user_input}"
    )

    prompt = f"""
    関連記憶:
    {retrieved_memory}

    会話履歴:
    {'\n'.join(history)}

    関連記憶を必要に応じて利用しながら回答してください。
    """

    print("\n===== PROMPT =====")
    print(prompt)
    print("==================\n")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    answer = response.text

    print(f"AI > {answer}")

    history.append(
        f"AI: {answer}"
    )