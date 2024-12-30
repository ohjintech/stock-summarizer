import requests
import os
from openai import OpenAI


url = "https://api.perplexity.ai/chat/completions"

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

def generate_answer(ticker):

    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant and you need to "
                "engage in a helpful, detailed, polite conversation with a user."
            ),
        },
        {   
            "role": "user",
            "content": (
                f"Generate a late night news type of report of {ticker} stock, providing this week's updates on the company as well as the related industry."
            ),
        },
    ]

    client = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")

    # chat completion without streaming
    response = client.chat.completions.create(
        model="llama-3.1-sonar-large-128k-online",
        messages=messages,
    )

    # Extract the text from the response
    response_text = response.choices[0].message.content

    # Write the response to a file
    with open('perplexity_response.txt', 'w') as file:
        file.write(response_text)

    # # chat completion with streaming
    # response_stream = client.chat.completions.create(
    #     model="llama-3.1-sonar-large-128k-online",
    #     messages=messages,
    #     stream=True,
    # )
    # for response in response_stream:
    #     print(response)


def perplexity_engine():

    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": "How many stars are there in our galaxy?"
            }
        ],
        "max_tokens": 2,
        "temperature": 0.2,
        "top_p": 0.9,
        "search_domain_filter": ["perplexity.ai"],
        "return_images": False,
        "return_related_questions": False,
        "search_recency_filter": "month",
        "top_k": 0,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 1
    }
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)        

    return response.text