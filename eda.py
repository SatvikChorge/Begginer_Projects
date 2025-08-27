import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("superstore.csv")

# 1. Basic Info
print("\n--- Dataset Info ---")
print(df.info())
print("\n--- First 5 Rows ---")
print(df.head())

# 2. Summary Statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# 3. Missing Values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 4. Sales Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Sales'], bins=20, kde=True)
plt.title("Sales Distribution")
plt.show()

# 5. Profit vs Discount
plt.figure(figsize=(8,5))
sns.scatterplot(x='Discount', y='Profit', data=df, hue='Category')
plt.title("Profit vs Discount")
plt.show()

# 6. Sales by Category
plt.figure(figsize=(6,4))
sns.barplot(x='Category', y='Sales', data=df, estimator=sum)
plt.title("Total Sales by Category")
plt.show()

# 7. Sales by Region
plt.figure(figsize=(6,4))
sns.barplot(x='Region', y='Sales', data=df, estimator=sum)
plt.title("Total Sales by Region")
plt.show()
