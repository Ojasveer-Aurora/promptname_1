import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
file_path = 'fifa_eda_stats.csv'  # Replace with your file path
df = pd.read_csv(file_path)



countries_to_highlight = ['Germany', 'Argentina', 'England']

nationality_counts = df['Nationality'].value_counts()

highlighted_counts = nationality_counts[countries_to_highlight]
other_counts = nationality_counts[~nationality_counts.index.isin(countries_to_highlight)].sum()
highlighted_counts['Other'] = other_counts

# Plot a pie chart
plt.figure(figsize=(10, 10))
plt.pie(highlighted_counts, labels=highlighted_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Players by Nationality')
plt.show()