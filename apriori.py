import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Load the Excel file
file_path = "cleaned_retail.xlsx"  # Replace with your file path
data = pd.read_excel(file_path)

# Step 2a: Convert the 'Item' column to strings
data['StockCode'] = data['StockCode'].astype(str)

# Step 2b: Preprocess the dataset
# Convert the 'Items' column into a list of lists (transactions)
transactions = data.groupby('InvoiceNo')['StockCode'].apply(list).tolist()

# Step 3: Convert transactions into one-hot encoded format
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Step 4: Apply the Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.009, use_colnames=True)

# Step 5: Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)  # Lowered to 0.2

# Step 6: Display the results
print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)

# Save
if not frequent_itemsets.empty:
    frequent_itemsets.to_csv("frequent_itemsets.csv", index=False)
if not rules.empty:
    rules.to_csv("association_rules.csv", index=False)