from openai import OpenAI
import os

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

res = client.fine_tuning.jobs.create(
  training_file="file-L8cMYIP80kfu9s38gItQsTMO", # ここに file ID をコピー
  model="gpt-3.5-turbo"
)
print( res.id )