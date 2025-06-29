import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_distribution(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df['Price'].dropna(), bins=30, kde=True, ax=ax)
    ax.set_title("Price Distribution")
    ax.set_xlabel("Price")
    ax.set_ylabel("Count")
    fig.tight_layout()
    return fig

def plot_brand_counts(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    brand_counts = df['Brand'].value_counts().head(15)
    sns.barplot(x=brand_counts.index, y=brand_counts.values, palette="magma", ax=ax)
    ax.set_title("Top 15 Brands by Product Count")
    ax.set_ylabel("Product Count")
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    return fig

def plot_avg_rating_per_brand(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    avg_ratings = df.groupby("Brand")["Rating"].mean().sort_values(ascending=False).head(15)
    sns.barplot(x=avg_ratings.index, y=avg_ratings.values, palette="viridis", ax=ax)
    ax.set_title("Top 15 Brands by Average Rating")
    ax.set_ylabel("Average Rating")
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    return fig

def plot_stock_status(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    status_counts = df['Availability'].value_counts()
    sns.barplot(x=status_counts.index, y=status_counts.values, palette="cool", ax=ax)
    ax.set_title("Stock Status Distribution")
    ax.set_ylabel("Count")
    fig.tight_layout()
    return fig

def plot_price_vs_rating(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x="Rating", y="Price", hue="Brand", legend=False, alpha=0.7, ax=ax)
    ax.set_title("Price vs Rating")
    fig.tight_layout()
    return fig

def plot_discount_analysis(df):
    df = df.dropna(subset=['Price', 'Original Price']).copy()
    df["Discount"] = df["Original Price"] - df["Price"]
    top_discounts = df.sort_values("Discount", ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_discounts["Title"], y=top_discounts["Discount"], palette="rocket", ax=ax)
    ax.set_title("Top 10 Products with Highest Discount")
    ax.set_ylabel("Discount")
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    return fig
