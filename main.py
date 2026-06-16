import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

history = []
long_term_memory = []

while True:
    user_input = input("You > ")
    
    if user_input == "exit":
        break

    if "私の名前は" in user_input:
        long_term_memory.append(user_input)

    print("\n===== LONG TERM MEMORY =====")
    print(long_term_memory)
    print("============================\n")


    history.append(
        f"User: {user_input}"
    )

    memory_text = "\n".join(long_term_memory)

    prompt = f"""
    長期記憶:
    {memory_text}

    会話履歴:
    {'\n'.join(history)}
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