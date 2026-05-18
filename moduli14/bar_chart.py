import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import lineStyles

from moduli13.kaggle_dataset import filtered_df

df = pd.read_csv("file1.csv")

filtered_df = df[df["avarage IQ"] >=100]

filtered_df = filtered_df.sort_values(by="avarage IQ", ascending= False)
print(filtered_df)

plt.figure(figsize=(14,8))

bars = plt.bar(filtered_df["Country"], filtered_df["avarage IQ"], color="skyblue")

plt.title("Avarage IQ per Country (IQ>=100)", fontsize=16)

plt.xlabel("Counry", fontsize=14)
plt.ylabel("avarage IQ",fontsize=14)

plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)

plt.grid(axis='y',lineStyles='_',alpha=0.8)

plt.bar_label(bars,fat='%.2f',fontsize=10,color="black")

plt.tight_layout()

plt.show()
