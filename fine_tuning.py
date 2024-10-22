from openai import OpenAI
import os

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

res = client.files.create(
  file=open("support.jsonl", "rb"),
  purpose="fine-tune"
)

print( res.id )
