import pandas as pd
from dotenv import load_dotenv
load_dotenv()

# your code here
df = pd.read_csv("data/raw/data.csv")
print(df.head())