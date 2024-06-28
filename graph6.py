import pandas as pd
import matplotlib.pyplot as plt

file_path = 'airbnb.csv'  
df = pd.read_csv(file_path)
criteria1 = (df['guests'] == 15) & (df['bedrooms'] == 1) & (df['beds'] == 2) & (df['bathrooms'] == 1)
criteria2 = (df['guests'] == 2) & (df['bedrooms'] == 1) & (df['beds'] == 1) & (df['bathrooms'] == 1)

countcriteria1 = df[criteria1].shape[0]
countcriteria2 = df[criteria2].shape[0]
count_other = df.shape[0] - countcriteria1 - countcriteria2
labels = ['Criteria-1', 'Criteria-2', 'Other']
sizes = [countcriteria1, countcriteria2, count_other]
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', )
plt.title('Airbnb Criterias')
plt.show()

