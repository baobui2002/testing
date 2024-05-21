import pandas as pd

# Create a DataFrame
data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Define a function to square a number
def square(x):
  return x * x

# Apply the function to each element of the DataFrame
squared_data = data.apply(square)

# Print the original and squared DataFrames
print("Original DataFrame:")
print(data)
print("\nSquared DataFrame:")
print(squared_data)
