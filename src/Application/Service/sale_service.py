from src.Infrastructure.Model.product import Product
from src.Infrastructure.Model.sale import Sale
from src.config.data_base import db
from sqlalchemy.exc import SQLAlchemyError

class SaleService:
    @staticmethod
    def create_sale(product_id, quantity, seller_id):
        try:
            product = Product.query.with_for_update().filter_by(id=product_id, seller_id=seller_id).first()

            if not product:
                return {"error": "Produto não encontrado ou não pertence a este vendedor.", "status": 404}

            if product.status != 'ATIVO':
                return {"error": "Produtos inativados não podem ser vendidos.", "status": 400}

            if product.quantity < quantity:
                return {"error": "Não é possível vender mais do que a quantidade disponível em estoque.", "status": 400}

            product.quantity -= quantity

            new_sale = Sale(
                product_id=product.id,
                seller_id=seller_id,
                quantity_sold=quantity,
                price_at_sale=product.price
            )

            db.session.add(new_sale)
            db.session.commit()

            return {"data": new_sale, "status": 201}

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Database Error on Sale: {e}")
            return {"error": "Ocorreu um erro no banco de dados ao processar a venda.", "status": 500}
        
    @staticmethod
    def get_all_by_seller(seller_id):
        try:
            sales = Sale.query.filter_by(seller_id=seller_id).order_by(Sale.sale_date.desc()).all()
            return [{
                "id": sale.id,
                "product_name": sale.product.name,
                "quantity": sale.quantity_sold,
                "price": sale.price_at_sale,
                "total": sale.quantity_sold * sale.price_at_sale,
                "date": sale.sale_date.isoformat()
            } for sale in sales]
        except SQLAlchemyError as e:
            print(f"Erro ao buscar vendas: {e}")
            return []