# DIP dependency inversion principle
# Los módulos de alto nivel (contiene la lógica importante del negocio - procesar pagos)
#    no deben depender de módulos de bajo nivel
#   (hace el trabajo técnico concreto - Enviar un correo con Gmail).
# Ambos deben depender de abstracciones.
from abc import ABC, abstractmethod


class EmailService:
    def send(self, msj: str):
        print(f"se ennvia este msj: {msj}")


class NotificacionService:
    def __init__(self) -> None:
        self.email_service = EmailService()

    def notify(self, msj: str):
        self.email_service.send(msj)


# ######################### Solucion  #########################


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailChannel(NotificationChannel):
    def send(self, message: str):
        print(f"Email enviado: {message}")


class SMSChannel(NotificationChannel):
    def send(self, message: str):
        print(f"SMS enviado: {message}")


class NotificationService:
    def __init__(self, channel: NotificationChannel):
        self.channel = channel

    def notify(self, message: str):
        self.channel.send(message)


email = EmailChannel()
notifier = NotificationService(email)
notifier.notify("Pago aprobado")

sms = SMSChannel()
notifier = NotificationService(sms)
notifier.notify("Pago aprobado")
