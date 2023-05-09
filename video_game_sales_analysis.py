import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("vgsales.csv")

# Explore and clean data
print(data.head())
print(data.isnull().sum())
data = data.dropna()

# Analyze top platforms and publishers
platform_counts = data["Platform"].value_counts().head(10)
sns.barplot(x=platform_counts.index, y=platform_counts.values)
plt.title("Top Platforms for Best-selling Games")
plt.xlabel("Platform")
plt.ylabel("Number of Games")
plt.show()

publisher_counts = data["Publisher"].value_counts().head(10)
sns.barplot(x=publisher_counts.index, y=publisher_counts.values)
plt.title("Top Publishers for Best-selling Games")
plt.xlabel("Publisher")
plt.ylabel("Number of Games")
plt.xticks(rotation=45)
plt.show()

# Analyze game sales by year
yearly_sales = data.groupby("Year")["Global_Sales"].sum().reset_index()
sns.lineplot(x="Year", y="Global_Sales", data=yearly_sales)
plt.title("Game Sales by Year")
plt.xlabel("Year")
plt.ylabel("Global Sales")
plt.show()

# Analyze top-selling game genres
genre_counts = data["Genre"].value_counts()
sns.barplot(x=genre_counts.index, y=genre_counts.values)
plt.title("Top-selling Game Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Games")
plt.xticks(rotation=45)
plt.show()
