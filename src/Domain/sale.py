class SaleDomain:
    def __init__(self, id, product_id, seller_id, quantity_sold, price_at_sale, sale_date):
        self.id = id
        self.product_id = product_id
        self.seller_id = seller_id
        self.quantity_sold = quantity_sold
        self.price_at_sale = price_at_sale
        self.sale_date = sale_date

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "seller_id": self.seller_id,
            "quantity_sold": self.quantity_sold,
            "price_at_sale": self.price_at_sale,
            "sale_date": self.sale_date.isoformat() if self.sale_date else None
        }