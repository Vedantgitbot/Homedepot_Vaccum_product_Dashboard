import streamlit as st
from models import VacuumProduct
from Data_Cleaning import (
    load_data,
    create_dataframe,
)
from Graph import (
    plot_price_distribution,
    plot_brand_counts,
    plot_avg_rating_per_brand,
    plot_stock_status,
    plot_price_vs_rating,
    plot_discount_analysis,
)

st.set_page_config(page_title="Vacuum Product Dashboard", layout="wide")

products = load_data()
df = create_dataframe(products)

st.sidebar.title("🔍 Filters")
brands = ["All"] + sorted(df["Brand"].dropna().unique())
selected_brand = st.sidebar.selectbox("Filter by Brand", brands)

filtered_df = df if selected_brand == "All" else df[df["Brand"] == selected_brand]

st.title("🧹 HomeDepot Vacuum Product Dashboard")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Price", f"${filtered_df['Price'].mean():.2f}")
col2.metric("Avg Rating", f"{filtered_df['Rating'].mean():.2f} ⭐")
col3.metric("Total Products", len(filtered_df))

st.subheader("📋 Product Listings")
st.dataframe(filtered_df[["Brand", "Title", "Price", "Rating", "Availability"]].reset_index(drop=True), height=400)

st.subheader("📊 Visual Insights")
chart = st.selectbox(
    "Choose a chart to display",
    [
        "Price Distribution",
        "Top 15 Brands by Product Count",
        "Top 15 Brands by Average Rating",
        "Stock Status Distribution",
        "Price vs Rating Scatterplot",
        "Top 10 Products with Highest Discount"
    ]
)

if chart == "Price Distribution":
    st.pyplot(plot_price_distribution(filtered_df))
elif chart == "Top 15 Brands by Product Count":
    st.pyplot(plot_brand_counts(df))
elif chart == "Top 15 Brands by Average Rating":
    st.pyplot(plot_avg_rating_per_brand(df))
elif chart == "Stock Status Distribution":
    st.pyplot(plot_stock_status(df))
elif chart == "Price vs Rating Scatterplot":
    st.pyplot(plot_price_vs_rating(filtered_df))
elif chart == "Top 10 Products with Highest Discount":
    st.pyplot(plot_discount_analysis(filtered_df))

