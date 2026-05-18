import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import lineStyles

from moduli3.sets import color

df = pd.read_csv("file1.csv")

plt.figure(figsize=(10,6))

plt.scatter(df['Mean years of schooling - 2021'],df['avarage IQ'], color='purple',alpha=0.7)

plt.title("Scatter Plot")

plt.xlabel('Mean years of schooling - 2021')
plt.ylabel('Avarage IQ')

plt.grid(True,lineStyle='--',aplha=0.7)
plt.show()