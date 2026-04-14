from src.Domain.product import ProductDomain
from src.Infrastructure.Model.product import Product
from src.config.data_base import db

class ProductService:
    @staticmethod
    def create_product(name, price, quantity, image, seller_id):
        product = Product(name=name, price=price, quantity=quantity, image=image, seller_id=seller_id, status="ATIVO")
        db.session.add(product)
        db.session.commit()

        return ProductDomain(id=product.id, name=product.name, price=product.price, quantity=product.quantity, image=product.image, seller_id=product.seller_id, status=product.status)

    @staticmethod
    def update_product(product_id, data):
        product = Product.query.get(product_id)

        if not product:
            return None

        product.name = data.get('nome', seller.name)
        product.price = data.get('preco', seller.price)
        product.quantity = data.get('quantidade', seller.quantity)
        product.image = data.get('imagem', seller.image)
        db.session.commit()

        return ProductDomain(
            product.id, 
            product.name,
            product.seller_id, 
            product.price, 
            product.quantity, 
            product.image,  
            product.status
        )

    @staticmethod
    def select_all_products():
        products = Product.query.all()

        if not products:
            return None

        lista = []
        for product in products:
            lista.append(product.to_dict())
        return lista

    @staticmethod
    def show_product(product_id):
        product = Product.query.get(product_id)

        if not product:
            return None
        
        return product.to_dict()

    @staticmethod
    def deactivate_product(product_id):
        product = Product.query.get(product_id)

        if not product:
            return None

        product.status = "INATIVO"
        db.session.commit()

        return ProductDomain(
            product.id, 
            product.name,
            product.seller_id, 
            product.price, 
            product.quantity, 
            product.image,  
            product.status
        )