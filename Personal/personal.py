from Personal.persona import Persona

class Personal(Persona):
    def __init__(self, num_empleado, password, salario, nombre, apellido, identidad, telefono, correo):
        super().__init__(nombre, apellido, identidad, telefono, correo)
        self.num_empleado = num_empleado
        self.password = password
        self.salario = salario
        