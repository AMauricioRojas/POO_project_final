import tkinter as tk
from tkinter import messagebox
from user_view import UserApp
from products_view import ProductApp

class DashboardApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Panel principal - Bienvenido {username}")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self.root, text=f"Hola, {self.username} 👋", font=("Arial", 18, "bold")).pack(pady=20)

        tk.Label(self.root, text="Selecciona una opción:", font=("Arial", 14)).pack(pady=10)

        # Botones principales
        tk.Button(self.root, text="👤 Gestionar Usuarios", font=("Arial", 12), width=25, height=2,command=self.abrir_usuarios).pack(pady=10)

        tk.Button(self.root, text="📦 Gestionar Productos", font=("Arial", 12), width=25, height=2,command=self.abrir_productos).pack(pady=10)

        tk.Button(self.root, text="🚪 Cerrar sesión", font=("Arial", 12), width=25, height=2,command=self.cerrar_sesion).pack(pady=10)

    def abrir_usuarios(self):
        self.root.destroy()
        app = UserApp(self.username)
        app.run()

    def abrir_productos(self):
        self.root.destroy()
        app = ProductApp(self.username)
        app.run()

    def cerrar_sesion(self):
        if messagebox.askyesno("Confirmar", "¿Deseas cerrar sesión?"):
            self.root.destroy()
            from login_view import LoginApp
            LoginApp().run()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    DashboardApp("admin").run()
