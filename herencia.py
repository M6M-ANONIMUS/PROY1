 Clase base para una Casa genérica
class Casa:
    def _init_(self, ventanas, puertas, techo, tipo_techo="a dos aguas"):
        """
        Inicializa una Casa con características básicas.

        Args:
            ventanas (int): Número de ventanas.
            puertas (int): Número de puertas.
            techo (str): Material del techo (ej: "teja", "lámina").
            tipo_techo (str): Tipo de techo (ej: "a dos aguas", "plana").
        """
        self.ventanas = ventanas
        self.puertas = puertas
        self.techo = techo
        self.tipo_techo = tipo_techo
        self.tipo_vivienda = "Genérica" # Atributo para identificar el tipo

    def mostrar_caracteristicas(self):
        """Muestra las características de la casa."""
        print(f"Tipo de vivienda: {self.tipo_vivienda}")
        print(f"  Ventanas: {self.ventanas}")
        print(f"  Puertas: {self.puertas}")
        print(f"  Techo: {self.techo}")
        print(f"  Tipo de techo: {self.tipo_techo}")

# Clase derivada para una Vivienda Familiar
class Vivienda_Familiar(Casa):
    def _init_(self, ventanas, puertas, techo, tipo_techo="a dos aguas", jardin=True, pisos=1):
        """
        Inicializa una Vivienda Familiar. Hereda de Casa y añade características.

        Args:
            ventanas (int): Número de ventanas.
            puertas (int): Número de puertas.
            techo (str): Material del techo.
            tipo_techo (str): Tipo de techo.
            jardin (bool): Indica si tiene jardín.
            pisos (int): Número de pisos.
        """
        super()._init_(ventanas, puertas, techo, tipo_techo) # Llama al constructor de la clase base
        self.tipo_vivienda = "Vivienda Familiar"
        self.jardin = jardin
        self.pisos = pisos

    def mostrar_caracteristicas(self):
        """Muestra las características específicas de la Vivienda Familiar."""
        super().mostrar_caracteristicas() # Muestra las características base
        print(f"  Tiene jardín: {'Sí' if self.jardin else 'No'}")
        print(f"  Pisos: {self.pisos}")

# Clase derivada para un Apartamento
class Apartamento(Casa):
    def _init_(self, ventanas, puertas, techo="hormigón", tipo_techo="plana", piso_edificio=None, numero_apartamento=None):
        """
        Inicializa un Apartamento. Hereda de Casa y modifica/añade características.

        Args:
            ventanas (int): Número de ventanas.
            puertas (int): Número de puertas.
            techo (str): Material del techo (por defecto hormigón para un edificio).
            tipo_techo (str): Tipo de techo (por defecto plana para un edificio).
            piso_edificio (int, optional): El piso en el que se encuentra el apartamento.
            numero_apartamento (str, optional): Número o identificador del apartamento.
        """
        super()._init_(ventanas, puertas, techo, tipo_techo) # Llama al constructor de la clase base
        self.tipo_vivienda = "Apartamento"
        self.piso_edificio = piso_edificio
        self.numero_apartamento = numero_apartamento

    def mostrar_caracteristicas(self):
        """Muestra las características específicas del Apartamento."""
        super().mostrar_caracteristicas() # Muestra las características base
        if self.piso_edificio is not None:
            print(f"  Ubicado en piso: {self.piso_edificio}")
        if self.numero_apartamento is not None:
            print(f"  Número de apartamento: {self.numero_apartamento}")

# Clase derivada para un Búngalo
class Bungalo(Casa):
    def _init_(self, ventanas, puertas, techo, tipo_techo="a dos aguas", piscina_privada=False):
        """
        Inicializa un Búngalo. Hereda de Casa y añade características.

        Args:
            ventanas (int): Número de ventanas.
            puertas (int): Número de puertas.
            techo (str): Material del techo.
            tipo_techo (str): Tipo de techo.
            piscina_privada (bool): Indica si tiene piscina privada.
        """
        super()._init_(ventanas, puertas, techo, tipo_techo) # Llama al constructor de la clase base
        self.tipo_vivienda = "Búngalo"
        self.piscina_privada = piscina_privada

    def mostrar_caracteristicas(self):
        """Muestra las características específicas del Búngalo."""
        super().mostrar_caracteristicas() # Muestra las características base
        print(f"  Tiene piscina privada: {'Sí' if self.piscina_privada else 'No'}")

# --- Ejemplo de uso ---
if __name__ == "_main_":
    # Crear instancias de diferentes tipos de casas
    mi_casa_familiar = Vivienda_Familiar(ventanas=10, puertas=2, techo="teja", pisos=2, jardin=True)
    mi_apartamento = Apartamento(ventanas=5, puertas=1, piso_edificio=7, numero_apartamento="7B")
    mi_bungalo = Bungalo(ventanas=8, puertas=3, techo="lámina", tipo_techo="plana", piscina_privada=True)
    casa_generica = Casa(ventanas=4, puertas=1, techo="cartón", tipo_techo="plana") # Una casa base

    # Mostrar las características de cada una
    print("--- Características de las viviendas ---")
    mi_casa_familiar.mostrar_caracteristicas()
    print("-" * 20)
    mi_apartamento.mostrar_caracteristicas()
    print("-" * 20)
    mi_bungalo.mostrar_caracteristicas()
    print("-" * 20)
    casa_generica.mostrar_caracteristicas()
    print("-" * 20)
