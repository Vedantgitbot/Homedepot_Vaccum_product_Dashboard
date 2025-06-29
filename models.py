class VacuumProduct:
    def __init__(self, timestamp, pid, brand, title, price, original_price, rating, reviews, availability):
        self.timestamp = timestamp
        self.pid = pid
        self.brand = brand.strip() if brand else None
        self.title = title.strip() if title else None
        self.price = price
        self.original_price = original_price
        self.rating = rating
        self.reviews = reviews
        self.availability = availability.strip().title() if availability else None

    @classmethod
    def from_dict(cls, data):
        try:
            return cls(
                timestamp=data.get('timestamp'),
                pid=data.get('product_id'),
                brand=data.get('brand'),
                title=data.get('title'),
                price=cls._safe_float(data.get('price')),
                original_price=cls._safe_float(data.get('original_price')),
                rating=cls._safe_float(data.get('rating')),
                reviews=cls._safe_int(data.get('review_count')),
                availability=data.get('stock_status')
            )
        except Exception as e:
            print(f"Error parsing row: {e}")
            return None

    @staticmethod
    def _safe_float(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return None

    @staticmethod
    def _safe_int(value):
        try:
            return int(value)
        except (TypeError, ValueError):
            return 0
