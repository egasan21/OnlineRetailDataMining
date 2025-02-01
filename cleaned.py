import pandas as pd

# Load the Excel file
file_path = 'Online Retail.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Remove rows with null values
df_cleaned = df.dropna()

# Save the cleaned data to a new Excel file
output_file_path = 'cleaned_retail.xlsx'  # Replace with your desired output file path
df_cleaned.to_excel(output_file_path, index=False)

print(f"Cleaned data saved to {output_file_path}")