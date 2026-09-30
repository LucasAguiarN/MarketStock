import pytest
from tests.sellerServiceFake import SellerServiceFake


@pytest.fixture
def sellerService():
    #Preparação
    sellerService = SellerServiceFake()
    sellerService.create_seller('Mercado Teste', '12.345.678/0001-90', 'teste@mercado.com', 'senha123', '11986687974')
    return sellerService

def test_authenticate_seller(sellerService):
    #Ação
    seller = sellerService.authenticate_seller('teste@mercado.com', 'senha123')
    #Verificação
    print(f'\nVendedor: {seller.name} | ID: {seller.id} | Total cadastrados: {len(sellerService.sellers)}')
    assert seller.name == 'Mercado Teste'
    assert seller.id == 1
    assert len(sellerService.sellers) == 1


def test_authenticate_seller_senha_incorreta(sellerService):
    #Ação
    seller = sellerService.authenticate_seller('teste@mercado.com', 'senha_errada')
    #Verificação
    print(f'\nVendedor: {seller} | Total cadastrados: {len(sellerService.sellers)}')
    assert seller is None

def test_authenticate_seller_email_nao_cadastrado(sellerService):
    #Ação
    seller = sellerService.authenticate_seller('teste2@mercado.com', 'senha123')
    #Verificação
    print(f'\nVendedor: {seller} | Total cadastrados: {len(sellerService.sellers)}')
    assert seller is None