import pandas as pd

customers = pd.read_csv('../data/customers.csv')
transactions = pd.read_csv('../data/transactions.csv')
events = pd.read_csv('../data/events.csv')

revenue = transactions.groupby('customer_id')['amount'].sum().reset_index()
engagement = events.groupby('customer_id').size().reset_index(name='events')

df = customers.merge(revenue, on='customer_id', how='left')
df = df.merge(engagement, on='customer_id', how='left')

print(df)
