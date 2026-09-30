"""
    Fake
    Substitui o SellerService real por uma implementação simples em memória (elimina uso de banco de dados e bcrypt) 
    Nos testes ele guarda os vendedores numa lista, permitindo cadastrar com create_seller e autenticar com authenticate_seller
"""
from src.Application.Service.seller_service import SellerService
from src.Domain.seller import SellerDomain


class SellerServiceFake(SellerService):
    def __init__(self):
        self.sellers = []

    def create_seller(self, name, cnpj, email, password, cellphone):
        seller = SellerDomain(len(self.sellers) + 1, name, cnpj, email, password, cellphone, 'ativo')
        self.sellers.append(seller)
        return seller

    def authenticate_seller(self, email, password):
        for seller in self.sellers:
            if seller.email == email and seller.password == password:
                return seller
        return None
