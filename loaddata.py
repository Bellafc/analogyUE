# from datasets import load_dataset
# ds = load_dataset("openai/gsm8k", "socratic")
# ds_small = ds["train"].select(range(200))
# ds_small.to_csv("gms8k200.csv")
# print(ds_small[:3])

# from datasets import load_dataset
# # Login using e.g. `huggingface-cli login` to access this dataset
# ds = load_dataset("open-r1/codeforces")
# ds_small = ds["train"].select(range(200))
# ds_small.to_csv("codeforces200.csv")
# print(ds_small[:3])

# import pandas as pd
#
# df = pd.read_parquet(r"C:\Users\ASUS\Downloads\train-00000-of-00011.parquet")
# print(df.head())
# df.to_csv("codeforces200.csv")
import json
import pandas as pd

# 文件路径
file_path = r"C:\Users\ASUS\Downloads\task.json"

# 读取 JSON 文件
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取 examples 字段并转换为 DataFrame
examples = data['examples']
df = pd.DataFrame(examples)
df.to_csv("factcheck.csv")
# 查看结果
print(df.head())
