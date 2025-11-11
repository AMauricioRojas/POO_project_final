import tkinter as tk
from tkinter import messagebox
from auth_controller import validar_credenciales
from user_view import DashboardApp

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de sesión")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        self.root.configure(bg="white")

        tk.Label(self.root, text="Bienvenido al sistema", font=("Arial", 16, "bold"), bg="white").pack(pady=15)
        tk.Label(self.root, text="Usuario:", bg="white").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Contraseña:", bg="white").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Iniciar sesión", command=self.login).pack(pady=10)

    def login(self):
        usuario = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showwarning("Faltan datos", "Ingresa usuario y contraseña")
            return

        if validar_credenciales(usuario, password):
            messagebox.showinfo("Acceso permitido", f"Bienvenido {usuario}")
            self.root.destroy()
            DashboardApp(usuario)
        else:
            messagebox.showerror("Acceso denegado", "Datos incorrectos")
