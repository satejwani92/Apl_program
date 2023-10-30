import pandas as  pd  

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 22, 35, 28],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']}

df = pd.DataFrame(data)

# Display the entire DataFrame
print("DataFrame:")
print(df)

# Select a specific column
ages = df['Age']
print("\nAges:")
print(ages)

# Filter the DataFrame based on a condition
young_people = df[df['Age'] < 30]
print("\nYoung People:")
print(young_people)

# Calculate basic statistics
average_age = df['Age'].mean()
print("\nAverage Age:", average_age)

# Sort the DataFrame by a column
sorted_df = df.sort_values(by='Age')
print("\nSorted DataFrame by Age:")
print(sorted_df)
