def generate_insight(row):
    if row['amount'] > 150:
        return "High-value customer"
    elif row['events'] < 2:
        return "Low engagement - churn risk"
    else:
        return "Moderate activity"

# Apply logic (mock AI layer)
