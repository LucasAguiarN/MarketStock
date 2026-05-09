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
    def update_product(product_id, data, seller_id):
        product = Product.query.filter_by(id=product_id, seller_id=seller_id).first()

        if not product:
            return None

        product.name = data.get('nome', product.name)
        product.price = data.get('preco', product.price)
        product.quantity = data.get('quantidade', product.quantity)
        product.image = data.get('imagem', product.image)
        db.session.commit()

        return ProductDomain(
            id=product.id,
            name=product.name,
            price=product.price,
            quantity=product.quantity,
            image=product.image,
            seller_id=product.seller_id,
            status=product.status
        )

    @staticmethod
    def select_all_products(seller_id):
        products = Product.query.filter_by(seller_id=seller_id).all()

        if not products:
            return []

        lista = []
        for product in products:
            lista.append(ProductDomain(
                id=product.id,
                name=product.name,
                price=product.price,
                quantity=product.quantity,
                image=product.image,
                seller_id=product.seller_id,
                status=product.status
            ))
        return lista

    @staticmethod
    def show_product(product_id, seller_id):
        product = Product.query.filter_by(id=product_id, seller_id=seller_id).first()

        if not product:
            return None
        
        return ProductDomain(
            id=product.id,
            name=product.name,
            price=product.price,
            quantity=product.quantity,
            image=product.image,
            seller_id=product.seller_id,
            status=product.status
        )

    @staticmethod
    def deactivate_product(product_id, seller_id):
        product = Product.query.filter_by(id=product_id, seller_id=seller_id).first()

        if not product:
            return None, False

        if product.status == "ATIVO":
            status_disabled = False
            product.status = "INATIVO"
            db.session.commit()
        else:
            status_disabled = True
        
        product_domain = ProductDomain(
            id=product.id,
            name=product.name,
            price=product.price,
            quantity=product.quantity,
            image=product.image,
            seller_id=product.seller_id,
            status=product.status,
        )
        return product_domain, status_disabled
