import pandas as pd

sheet_id = '1NlHTroeZKG2qktfvGesTemmfj-qvhigEls__emyqdRw'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'
df = pd.read_csv(url)

print(df)