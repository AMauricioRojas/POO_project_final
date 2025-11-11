# ExamenPOO_Apellido_Nombre.py
# Sistema básico de biblioteca - POO con herencia y polimorfismo
from datetime import date, timedelta
from typing import Optional, List

class Libro:
    def __init__(self, titulo: str, autor: str, anio: int, codigo: str, disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.codigo = codigo
        self.disponible = disponible

    def mostrar_info(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Libro[{self.codigo}] '{self.titulo}' - {self.autor} ({self.anio}) | {estado}"

    def marcar_como_prestado(self):
        self.disponible = False

    def marcar_como_disponible(self):
        self.disponible = True

    def esta_disponible(self) -> bool:
        return self.disponible


class Usuario:
    def __init__(self, nombre: str, id_usuario: str, correo: str):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.correo = correo
        # lista de préstamos asociados al usuario
        self.prestamos: List['Prestamo'] = []

    def mostrar_info(self) -> str:
        return f"Usuario[{self.id_usuario}] {self.nombre} - {self.correo}"

    def solicitar_prestamo(self, libro: Libro, prestamos_global: List['Prestamo'], dias: int = 14) -> Optional['Prestamo']:
        if libro.esta_disponible():
            nuevo = Prestamo(libro=libro, usuario=self)
            nuevo.registrar_prestamo(dias=dias)
            prestamos_global.append(nuevo)
            self.prestamos.append(nuevo)
            return nuevo
        else:
            print(f"[INFO] El libro '{libro.titulo}' no está disponible para préstamo.")
            return None


class Estudiante(Usuario):
    def __init__(self, nombre: str, id_usuario: str, correo: str, carrera: str, semestre: int):
        super().__init__(nombre, id_usuario, correo)
        self.carrera = carrera
        self.semestre = semestre

    def mostrar_info(self) -> str:
        base = super().mostrar_info()
        return f"{base} | Estudiante - {self.carrera}, Sem: {self.semestre}"


class Profesor(Usuario):
    def __init__(self, nombre: str, id_usuario: str, correo: str, departamento: str, tipo_contrato: str):
        super().__init__(nombre, id_usuario, correo)
        self.departamento = departamento
        self.tipo_contrato = tipo_contrato

    def mostrar_info(self) -> str:
        base = super().mostrar_info()
        return f"{base} | Profesor - {self.departamento}, Contrato: {self.tipo_contrato}"


class Prestamo:
    def __init__(self, libro: Libro, usuario: Usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo: Optional[date] = None
        self.fecha_devolucion: Optional[date] = None  # fecha límite
        self.fecha_entrega: Optional[date] = None  # fecha real de entrega (cuando devuelva)

    def registrar_prestamo(self, dias: int = 14):
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=dias)
        self.libro.marcar_como_prestado()
        print(f"[PRESTAMO] Registrado: {self.usuario.nombre} -> '{self.libro.titulo}' | Fecha préstamo: {self.fecha_prestamo} | Dev.: {self.fecha_devolucion}")

    def devolver_libro(self):
        if self.libro.esta_disponible():
            print("[AVISO] Este libro ya está marcado como disponible. Revisa registros.")
            return
        self.fecha_entrega = date.today()
        self.libro.marcar_como_disponible()
        print(f"[DEVOLUCION] '{self.libro.titulo}' devuelto por {self.usuario.nombre} el {self.fecha_entrega}")

    def mostrar_info(self) -> str:
        fp = self.fecha_prestamo.isoformat() if self.fecha_prestamo else "N/A"
        fd = self.fecha_devolucion.isoformat() if self.fecha_devolucion else "N/A"
        fe = self.fecha_entrega.isoformat() if self.fecha_entrega else "No devuelto"
        return f"Prestamo: Libro[{self.libro.codigo}] '{self.libro.titulo}' | Usuario[{self.usuario.id_usuario}] {self.usuario.nombre} | Prest: {fp} | Dev limite: {fd} | Entrega: {fe}"


# --------------------------
# Simulación / Ejecución
# --------------------------
def main():
    prestamos_global: List[Prestamo] = []

    # Crear libros (al menos 2)
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "LIB001")
    libro2 = Libro("Introducción a Python", "Autor Ejemplo", 2020, "LIB002")
    libro3 = Libro("Estructuras de Datos", "A. Programador", 2018, "LIB003")

    # Crear usuarios (2 estudiantes y 2 profesores)
    estudiante1 = Estudiante("Ana Pérez", "EST001", "ana.perez@uni.edu", "Sistemas", 6)
    estudiante2 = Estudiante("Juan López", "EST002", "juan.lopez@uni.edu", "Ingeniería", 3)

    profesor1 = Profesor("Dra. María Ruiz", "PROF001", "m.ruiz@uni.edu", "Matemáticas", "Tiempo completo")
    profesor2 = Profesor("Dr. Carlos Gómez", "PROF002", "c.gomez@uni.edu", "Informática", "Tiempo parcial")

    # Mostrar info (demostración polimorfismo)
    print("=== USUARIOS ===")
    usuarios = [estudiante1, estudiante2, profesor1, profesor2]
    for u in usuarios:
        print(u.mostrar_info())  # polimorfismo: cada clase muestra diferente

    # Mostrar libros
    print("\n=== LIBROS ===")
    for lb in [libro1, libro2, libro3]:
        print(lb.mostrar_info())

    # Simular préstamos
    print("\n=== SIMULACIÓN DE PRÉSTAMOS ===")
    # Estudiante 1 solicita libro1
    prest1 = estudiante1.solicitar_prestamo(libro1, prestamos_global, dias=21)
    # Profesor 1 solicita libro2
    prest2 = profesor1.solicitar_prestamo(libro2, prestamos_global, dias=30)

    # Intento de préstamo cuando libro ya no está disponible
    prest3 = estudiante2.solicitar_prestamo(libro1, prestamos_global, dias=14)  # debe indicar no disponible

    # Mostrar estado préstamos
    print("\n=== PRÉSTAMOS REGISTRADOS ===")
    for p in prestamos_global:
        print(p.mostrar_info())

    # Devolver un libro
    print("\n=== DEVOLUCIÓN ===")
    if prest1:
        prest1.devolver_libro()

    # Mostrar estado final de libros y préstamos
    print("\n=== ESTADO FINAL LIBROS ===")
    for lb in [libro1, libro2, libro3]:
        print(lb.mostrar_info())

    print("\n=== ESTADO FINAL PRÉSTAMOS ===")
    for p in prestamos_global:
        print(p.mostrar_info())


if __name__ == "__main__":
    main()
