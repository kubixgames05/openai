import random
import openai


openai.api_key = "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"
model_engine = "code-davinci-002"

def generate_response(question, eng):
    prompt = f"Q: {question}\nA:"
    response = openai.Completion.create(
        engine=eng,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

while(1):
    a = int(input("0: text-davinci-003\n1: gpt-3.5-turbo\nPodaj silnik: "))
    if a==0:
        question = str(input("Pytanie: "))
        eng = "text-davinci-003"
        response = generate_response(question, eng)
        print(f"Odpowiedź to: {response}")
    elif a==1:
        messages = [
                    {"role": "system", "content": "You are a chatbot"},
                    {"role": "user", "content": str(input("Pytanie: "))},
                ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        result = ''
        for choice in response.choices:
            result += choice.message.content
        print(result)
    else:  
        print("Zły silnik")