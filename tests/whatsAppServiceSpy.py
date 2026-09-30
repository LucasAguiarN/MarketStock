"""
    SPY
    Substitui o serviço externo do WhatsApp (Twilio)
    Nos testes ele não envia mensagens reais e registra quantas vezes send_message foi chamado e com quais argumentos
"""
from src.Infrastructure.http.whats_app import WhatsAppService


class WhatsAppServiceSpy(WhatsAppService):
    def __init__(self):
        self.__contagem_envios = 0
        self.__ultimo_numero = None
        self.__ultima_mensagem = None

    def send_message(self, to, message):
        self.__contagem_envios += 1
        self.__ultimo_numero = to
        self.__ultima_mensagem = message

    def numero_de_envios(self):
        return self.__contagem_envios

    def ultimo_numero(self):
        return self.__ultimo_numero

    def ultima_mensagem(self):
        return self.__ultima_mensagem