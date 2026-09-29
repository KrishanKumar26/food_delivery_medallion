import pandas as pd



# ==========================================
# 1. EXTRACT
# ==========================================

input_path = "data/silver/food_orders.csv"

df = pd.read_csv(input_path)

print("silver data")
print(df)

# ==========================================
# 2. TRANSFORM
# ==========================================
# Calculate total sales for each order
df["total_sales"] = (
    df["quantity"] * df["price"]
)

# Calculate category-wise performance(sum,count,max etc)

gold_df = df.groupby("category").agg(
    total_orders=("order_id","count"),
     total_quantity=("quantity", "sum"),
    total_sales=("total_sales", "sum")
).reset_index()


# ==========================================
# 3. LOAD
# ==========================================
output_path = "data/gold/food_orders.csv"
gold_df.to_csv(
    output_path,
    index=False
)
print("\nGold data created successfully!")
print(f"Output: {output_path}")

print("\nGold data:")
print(gold_df)