import openai
import os

# OpenAI APIキーの設定
openai.api_key = os.getenv("OPENAI_API_KEY")

# ファインチューニングジョブの進行状況を確認
fine_tune_job_id = "ftjob-zSPcZF1Oo7erUgSglQGp3Xfc"  # 生成されたジョブIDを使用

fine_tune_status = openai.FineTune.retrieve(id=fine_tune_job_id)
print(f"Fine-tuning status: {fine_tune_status['status']}")
print(f"Fine-tuning job details: {fine_tune_status}")
