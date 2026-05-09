class ProductDomain():
    def __init__(self, id, seller_id, name, price, quantity, image, status='ATIVO'):
        self.id = id
        self.name = name
        self.price = price
        self.seller_id = seller_id
        self.quantity = quantity
        self.image = image
        self.status = status
    
    def to_dict(self):
        return {
            "id": self.id,
            "seller_id": self.seller_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "image": self.image,
            "status": self.status
        }