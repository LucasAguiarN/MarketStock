from src.config.data_base import db
from datetime import datetime

class Sale(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=False)
    quantity_sold = db.Column(db.Integer, nullable=False)
    price_at_sale = db.Column(db.Float, nullable=False)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relacionamentos
    product = db.relationship('Product', backref='sales')
    seller = db.relationship('Seller', backref='sales')

    def __init__(self, product_id, seller_id, quantity_sold, price_at_sale):
        self.product_id = product_id
        self.seller_id = seller_id
        self.quantity_sold = quantity_sold
        self.price_at_sale = price_at_sale

    def __repr__(self):
        return f'<Sale {self.id} - Product: {self.product_id} - Seller: {self.seller_id}>'