import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import lineStyles

df = pd.read_csv("file1.csv")

avg_iq_by_continent = df.groupby('Continent')('Avarage IQ').mean()

plt.figure(figsize= (10,6))

avg_iq_by_continent.plot(kind='line', marker='o', color='skyblue')

plt.title('avarage IQ by Continent')
plt.xlabel('continent')
plt.ylabel('avarage IQ')

plt.grid(axis='both', lineStyles='--', alpha=0.7)
plt.show()

