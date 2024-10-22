from openai import OpenAI
import os

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

res = client.files.create(
  file=open("support.jsonl", "rb"),
  purpose="fine-tune"
)


# アップロードしたファイルIDを出力
print("File ID: ", res.id)

# ファインチューニングジョブの作成
fine_tune_res = client.fine_tuning.create(
    model="gpt-4o-2024-08-06",  # ここでGPT-4を指定
    training_file=res.id,  # アップロードされたファイルIDを指定
    hyperparameters={
        "n_epochs": 3  # 必要に応じてエポック数やその他のハイパーパラメータを設定
    }
)

# ファインチューニングジョブのIDを出力
print("Fine-tuning Job ID: ", fine_tune_res.id)