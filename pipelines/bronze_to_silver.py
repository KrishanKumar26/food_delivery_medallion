import pandas as pd

# ==========================================
# 1. EXTRACT
# ==========================================
input_path = "data/bronze/food_orders.csv"
df = pd.read_csv(input_path)
print("Bronze data :")
print(df.head())

# ==========================================
# 2. TRANSFORM
# ==========================================

# remove dulpicate order(order_id jaaha per duplicate)
df = df.drop_duplicates(subset=["order_id"])
df = df.drop_duplicates(subset=["product_id"])

# Convert quantity to numeric
df["quantity"] = pd.to_numeric(
    df["quantity"],
    errors="coerce"
)

# Remove invalid quantity - Here some are -ve so remove this and take > 0 wale
# Quantity should be greater than 0

df = df[df["quantity"] > 0]

# ==========================================
# 3. LOAD
# ==========================================
output_path = "data/silver/food_orders.csv"
df.to_csv(
    output_path,
    index=False
)

print("\nSilver data created successfully!")
print(f"Output: {output_path}")

print("\nSilver data:")
print(df)