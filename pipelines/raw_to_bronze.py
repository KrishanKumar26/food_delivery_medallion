# Here we complete this medillion arti using panda we also do withthe help of,
# spark but vo databricks karne ke badd karege
import pandas as pd

# ==========================================
# 1. EXTRACT
# ==========================================

input_path = "data/raw/food_orders.csv"
df = pd.read_csv(input_path)
print("Row data :")
print(df.head())

# ==========================================
# 2. TRANSFORM
# ==========================================
# Bronze mein major business transformation nahi.
# Source data ko mostly preserve karenge.

bronze_df = df.copy() # thisis bronze layer

# ==========================================
# 3. LOAD
# ==========================================

output_path =  "data/bronze/food_orders.csv"
bronze_df.to_csv(
    output_path,
    index=False
)
print("Bronze data created successfully!")
print(f"Output: {output_path}")