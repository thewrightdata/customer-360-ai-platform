import pandas as pd

customers = pd.read_csv('../data/customers.csv')
transactions = pd.read_csv('../data/transactions.csv')
events = pd.read_csv('../data/events.csv')

print("Data loaded successfully")
