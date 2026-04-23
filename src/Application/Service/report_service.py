from datetime import datetime, timedelta
from sqlalchemy import func
from src.Infrastructure.Model.sale import Sale
from src.Infrastructure.Model.product import Product
from src.config.data_base import db

class ReportService:
    @staticmethod
    def get_sales_summary(seller_id, period='month'):
        today = datetime.utcnow().date()
        start_date = None

        if period == 'today':
            start_date = datetime.combine(today, datetime.min.time())
        elif period == 'week':
            start_date = datetime.combine(today - timedelta(days=today.weekday()), datetime.min.time())
        elif period == 'month':
            start_date = datetime.combine(today.replace(day=1), datetime.min.time())

        query = db.session.query(
            func.sum(Sale.quantity_sold * Sale.price_at_sale).label('total_revenue'),
            func.sum(Sale.quantity_sold).label('total_items_sold')
        ).filter(Sale.seller_id == seller_id)

        if start_date:
            query = query.filter(Sale.sale_date >= start_date)

        summary = query.one()

        total_revenue = summary.total_revenue or 0
        total_items_sold = summary.total_items_sold or 0

        return {
            "total_revenue": float(total_revenue),
            "total_items_sold": int(total_items_sold)
        }

    @staticmethod
    def get_top_selling_products(seller_id, limit=5):
        top_products = db.session.query(
            Product.id,
            Product.name,
            Product.image,
            func.sum(Sale.quantity_sold).label('total_sold')
        ).join(Product, Sale.product_id == Product.id)\
         .filter(Sale.seller_id == seller_id)\
         .group_by(Product.id, Product.name, Product.image)\
         .order_by(func.sum(Sale.quantity_sold).desc())\
         .limit(limit)\
         .all()

        return [
            {
                "product_id": product.id,
                "name": product.name,
                "image": product.image,
                "total_sold": int(product.total_sold)
            } for product in top_products
        ]

    @staticmethod
    def get_low_stock_products(seller_id, threshold=10):
        low_stock_products = Product.query.filter(
            Product.seller_id == seller_id,
            Product.status == 'ATIVO',
            Product.quantity <= threshold
        ).order_by(Product.quantity.asc()).all()

        return [
            {
                "product_id": product.id,
                "name": product.name,
                "current_quantity": product.quantity
            } for product in low_stock_products
        ]