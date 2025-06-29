import csv
import pandas as pd
from models import VacuumProduct

def load_data():
    products = []
    try:
        with open("/Users/vedantbrahmbhatt/Desktop/Home_Depot_Analysis/vacuum_dummy_data.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = VacuumProduct.from_dict(row)
                if product:
                    products.append(product)
    except Exception as e:
        print(f"Error loading data: {e}")
    return products

def create_dataframe(products):
    return pd.DataFrame([{
        "Timestamp": p.timestamp,
        "Product ID": p.pid,
        "Brand": p.brand,
        "Title": p.title,
        "Price": p.price,
        "Original Price": p.original_price,
        "Rating": p.rating,
        "Reviews": p.reviews,
        "Availability": p.availability
    } for p in products])
