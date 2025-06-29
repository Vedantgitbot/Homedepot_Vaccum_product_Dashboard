import tkinter as tk
from tkinter import ttk
from Data_Cleaning import create_dataframe
from Graph import (
    plot_price_distribution,
    plot_brand_counts,
    plot_avg_rating_per_brand,
    plot_stock_status,
    plot_price_vs_rating,
    plot_discount_analysis,
)

class VacuumGUI:
    def __init__(self, root, products):
        self.root = root
        self.root.title("HomeDepot Vacuum Product Dashboard")
        self.root.geometry("1000x600")
        self.products = products
        self.df = create_dataframe(products)

        self.selected_brand = tk.StringVar()
        self._build_ui()

    def _build_ui(self):
        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(top_frame, text="Filter by Brand:").pack(side="left", padx=5)

        brands = sorted(self.df['Brand'].dropna().unique())
        brand_dropdown = ttk.Combobox(top_frame, textvariable=self.selected_brand, values=["All"] + brands)
        brand_dropdown.current(0)
        brand_dropdown.pack(side="left")
        brand_dropdown.bind("<<ComboboxSelected>>", self.update_table)

        self.tree = ttk.Treeview(self.root, columns=("Brand", "Title", "Price", "Rating", "Availability"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.update_table()

        kpi_frame = ttk.LabelFrame(self.root, text="KPIs")
        kpi_frame.pack(fill="x", padx=10, pady=5)

        avg_price = self.df["Price"].mean()
        avg_rating = self.df["Rating"].mean()
        total_products = len(self.df)

        ttk.Label(kpi_frame, text=f"Avg Price: ${avg_price:.2f}").pack(side="left", padx=10)
        ttk.Label(kpi_frame, text=f"Avg Rating: {avg_rating:.2f} ⭐").pack(side="left", padx=10)
        ttk.Label(kpi_frame, text=f"Total Products: {total_products}").pack(side="left", padx=10)

        graph_frame = ttk.Frame(self.root)
        graph_frame.pack(pady=10)

        ttk.Button(graph_frame, text="📊 Price Distribution", command=lambda: plot_price_distribution(self.df)).pack(side="left", padx=5)
        ttk.Button(graph_frame, text="🏷 Brand Counts", command=lambda: plot_brand_counts(self.df)).pack(side="left", padx=5)
        ttk.Button(graph_frame, text="⭐ Avg Rating/Brand", command=lambda: plot_avg_rating_per_brand(self.df)).pack(side="left", padx=5)
        ttk.Button(graph_frame, text="📦 Stock Status", command=lambda: plot_stock_status(self.df)).pack(side="left", padx=5)
        ttk.Button(graph_frame, text="💸 Price vs Rating", command=lambda: plot_price_vs_rating(self.df)).pack(side="left", padx=5)
        ttk.Button(graph_frame, text="🔥 Discounts", command=lambda: plot_discount_analysis(self.df)).pack(side="left", padx=5)

    def update_table(self, event=None):
        brand_filter = self.selected_brand.get()
        for row in self.tree.get_children():
            self.tree.delete(row)

        filtered_df = self.df if brand_filter == "All" else self.df[self.df["Brand"] == brand_filter]

        for _, row in filtered_df.iterrows():
            self.tree.insert("", "end", values=(
                row["Brand"], row["Title"][:30] + "...", f"${row['Price']:.2f}" if row["Price"] else "N/A",
                f"{row['Rating']:.1f}" if row["Rating"] else "N/A", row["Availability"]
            ))
