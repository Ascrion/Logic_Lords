import pandas as pd

dataset = pd.read_csv('researchDataset.csv')

keywords = ['machine learning', 'neural networks', 'deep learning', 'AI']

def search_keywords_in_title(title, keywords):
    for keyword in keywords:
        if keyword.lower() in title.lower(): 
            return True
    return False

results = []
for index, row in dataset.iterrows():
    title = row['Title']
    if search_keywords_in_title(title, keywords):
        results.append({
            'Title': title,
            'Authors': row['Authors'],
            'Year': row['Year']
        })

if results:
    for result in results:
        print(f"Title: {result['Title']}")
        print(f"Authors: {result['Authors']}")
        print(f"Year: {result['Year']}\n")
else:
    print("No publications found for the given keywords.")

