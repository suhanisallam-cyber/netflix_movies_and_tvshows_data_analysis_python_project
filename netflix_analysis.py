# STEP 1: Import Necessary Libraries
# NumPy: Used for numerical operations and array manipulations
import numpy as np

# Pandas: Used for data handling, manipulation, and analysis (DataFrames)
import pandas as pd

# Matplotlib & Seaborn: Used for creating visual charts and graphs
import matplotlib.pyplot as plt
import seaborn as sns

# Set a clean and modern white grid style for seaborn plots
sns.set_theme(style="whitegrid")

# STEP 2: Load the Dataset

# Load the Netflix dataset CSV file downloaded from Kaggle
df = pd.read_csv("netflix_titles.csv")

# Display the first 5 rows to inspect the data structure
print("--- First 5 Rows ---")
print(df.head())

# STEP 3: Data Inspection & Cleaning

# Display dataset summary including data types and non-null counts
print("\n--- Dataset Info ---")
print(df.info())

# Check the count of missing (null) values in each column
print("\n--- Missing Values Count ---")
print(df.isnull().sum())

# Date format specify karke date_added convert karein
df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), format="mixed")

# Naya 'year_added' column
df["year_added"] = df["date_added"].dt.year

# inplace=True ki jagah direct assignment karein (Copy-on-Write warning fix)
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")


# STEP 4: Analysis & Visualizations


# 1. Count Plot: hue="type" add kiya warning remove karne ke liye
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="type", hue="type", palette="Set2", legend=False)
plt.title("Distribution of Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Total Count")
# Figure save kar rahe hain (plt.show se pehle)
plt.savefig("movies_vs_tvshows.png", dpi=300, bbox_inches="tight")
plt.show()

# 2. Bar Plot: hue="y" add kiya
top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(
    x=top_countries.values,
    y=top_countries.index,
    hue=top_countries.index,
    palette="magma",
    legend=False,
)
plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
# Figure save kar rahe hain
plt.savefig("top_10_countries.png", dpi=300, bbox_inches="tight")
plt.show()

# 3. Line Plot: Year-wise trend
content_by_year = df.groupby(["year_added", "type"]).size().unstack()

content_by_year.plot(kind="line", figsize=(10, 5), marker="o")
plt.title("Content Added on Netflix Over Time")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
# Figure save kar rahe hain
plt.savefig("content_addition_trend.png", dpi=300, bbox_inches="tight")
plt.show()