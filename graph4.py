import pandas as pd
import matplotlib.pyplot as plt

file_path = 'airbnb.csv' 
df = pd.read_csv(file_path)

def locationofairbnb(address):
    if 'Turkey' in address:
        return 'Turkey'
    elif 'New Delhi' in address:
        return 'New Delhi'
    elif 'Mumbai' in address:
        return 'Mumbai'
    else:
        return 'Other'


df['Categorized Location'] = df['address'].apply(locationofairbnb)


location_counts = df['Categorized Location'].value_counts()

plt.figure(figsize=(10, 10))
plt.pie(location_counts, labels=location_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Players by Nationality')

plt.show()