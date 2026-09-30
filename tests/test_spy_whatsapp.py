import pytest
from tests.whatsAppServiceSpy import WhatsAppServiceSpy


def test_envia_mensagem_whatsapp():
    #Preparação
    whatsApp = WhatsAppServiceSpy()                                           # Cria Objeto Spy
    #Ação
    whatsApp.send_message('11986687974', 'Seu código de ativação é: 1234')    # Método do Objeto Spy que gera a Mensagem
    #Verificação
    print(f'\nEnvios: {whatsApp.numero_de_envios()}\nNúmero: {whatsApp.ultimo_numero()}\nMensagem: {whatsApp.ultima_mensagem()}')
    assert whatsApp.numero_de_envios() == 1                                   # Assert Método Get do Objeto Spy
    assert whatsApp.ultimo_numero() == '11986687974'                          # Assert Método Get do Objeto Spy
    assert whatsApp.ultima_mensagem() == 'Seu código de ativação é: 1234'     # Assert Método Get do Objeto Spy
