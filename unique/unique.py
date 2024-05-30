import pandas as pd

# Load the CSV file
file_path = input("Enter the path to your CSV file: ")
df = pd.read_csv(file_path)

# Iterate over each column and print unique values
for column in df.columns:
    unique_values = df[column].unique()
    print(f"Unique values in column '{column}':")
    print(unique_values)
    print()
