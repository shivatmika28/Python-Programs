from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

while True:
    prompt = input("\nYou: ")

    if prompt.lower() == "quit":
        break

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print("\nGPT:", response.choices[0].message.content)
    
