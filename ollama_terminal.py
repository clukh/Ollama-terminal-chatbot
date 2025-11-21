from openai import OpenAI

def chat_with_gpt(api_key, prompt):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    api_key = input("Enter your OpenAI API Key: ")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break
        output = chat_with_gpt(api_key, user_input)
        print("GPT: " + output)
