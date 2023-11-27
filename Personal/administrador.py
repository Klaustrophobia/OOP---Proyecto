from .comprador import Comprador
from .vendedor import Vendedor

class Admnistrador (Comprador, Vendedor):
    def __init__(self):
        pass