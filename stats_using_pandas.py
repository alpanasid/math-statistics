import pandas as pd

# Sample data
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Values": [45, 67, 34, 89, 12, 49, 38, 56, 72, 81]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate mean and median
mean_value = df["Values"].mean()
median_value = df["Values"].median()

# Print results
print("Sample Data:")
print(df)
print("\nMean of Values:", mean_value)
print("Median of Values:", median_value)
