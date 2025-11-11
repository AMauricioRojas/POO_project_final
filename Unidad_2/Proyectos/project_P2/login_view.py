import tkinter as tk
from tkinter import messagebox
from auth_controller import validar_credenciales
from dashboard_view import DashboardApp


class LoginApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login - POO Project P2")
        self.root.geometry("350x200")
        self.root.resizable(False, False)

        tk.Label(self.root, text="Usuario:").pack(pady=(20,5))
        self.usuario_entry = tk.Entry(self.root)
        self.usuario_entry.pack()

        tk.Label(self.root, text="Contraseña:").pack(pady=(10,5))
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack()

        tk.Button(self.root, text="Ingresar", command=self.login).pack(pady=15)

    def login(self):
        usuario = self.usuario_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showerror("Error", "Por favor completa todos los campos.")
            return

        valido = validar_credenciales(usuario, password)
        if valido:
            messagebox.showinfo("Éxito", "Inicio de sesión correcto.")
            self.root.destroy()
            app = DashboardApp(usuario)
            app.run()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    LoginApp().run()
