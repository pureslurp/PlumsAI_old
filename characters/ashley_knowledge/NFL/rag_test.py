import pandas as pd
from openai import OpenAI
import os
import ast
import numpy as np
import pdb

client = OpenAI(api_key="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")

question = "What time zone is Michigan in?"

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input = [text], model=model).data[0].embedding

with open('characters/ashley_knowledge/NFL/2024/future_games_odds_list.txt', 'r') as file:
    contents = file.read()

print(get_embedding(contents))

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": question}
    ]
)

print(response.choices[0].message.content)