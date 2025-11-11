import tkinter as tk
from tkinter import ttk, messagebox
from user_controller import ver_usuarios, agregar_usuario, actualizar_usuario, eliminar_usuario

class DashboardApp:
    def __init__(self, usuario):
        # Crear nueva ventana raíz para el dashboard
        self.root = tk.Tk()
        self.root.title(f"Panel de administración - {usuario}")
        self.root.geometry("600x400")
        self.root.configure(bg="white")
        self.usuario = usuario

        self.crear_widgets()
        self.cargar_usuarios()
        self.root.mainloop()

    def crear_widgets(self):
        # Título y usuario conectado
        tk.Label(self.root, text=f"Usuario conectado: {self.usuario}", font=("Arial", 10, "italic"), bg="white").pack(pady=4)
        tk.Label(self.root, text="Gestión de Usuarios", font=("Arial", 16, "bold"), bg="white").pack(pady=8)

        # Frame con entradas
        frame = tk.Frame(self.root, bg="white")
        frame.pack(pady=6)

        tk.Label(frame, text="ID:", bg="white").grid(row=0, column=0, padx=6, pady=4)
        self.id_entry = tk.Entry(frame, width=8)
        self.id_entry.grid(row=0, column=1, padx=6, pady=4)

        tk.Label(frame, text="Username:", bg="white").grid(row=1, column=0, padx=6, pady=4)
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.grid(row=1, column=1, padx=6, pady=4)

        tk.Label(frame, text="Password:", bg="white").grid(row=2, column=0, padx=6, pady=4)
        self.password_entry = tk.Entry(frame, show="*", width=30)
        self.password_entry.grid(row=2, column=1, padx=6, pady=4)

        # Botones CRUD + Cerrar sesión
        botones = tk.Frame(self.root, bg="white")
        botones.pack(pady=8)

        tk.Button(botones, text="Agregar", width=10, command=self.agregar).grid(row=0, column=0, padx=6)
        tk.Button(botones, text="Actualizar", width=10, command=self.actualizar).grid(row=0, column=1, padx=6)
        tk.Button(botones, text="Eliminar", width=10, command=self.eliminar).grid(row=0, column=2, padx=6)
        tk.Button(botones, text="Refrescar", width=10, command=self.cargar_usuarios).grid(row=0, column=3, padx=6)
        tk.Button(botones, text="Cerrar sesión", width=12, command=self.cerrar_sesion).grid(row=0, column=4, padx=12)

        # Tabla de usuarios (se muestra solo en el dashboard)
        self.tabla = ttk.Treeview(self.root, columns=("ID", "Username", "Password"), show="headings", height=10)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Username", text="Username")
        self.tabla.heading("Password", text="Password")
        self.tabla.pack(pady=8, fill="both", expand=True, padx=10)

        # Cuando se selecciona una fila, cargar los datos en los entries
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)

    # Cargar datos desde la BD y mostrar en la tabla
    def cargar_usuarios(self):
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        usuarios = ver_usuarios()
        for u in usuarios:
            self.tabla.insert("", tk.END, values=u)

    # Agregar usuario (CREATE)
    def agregar(self):
        user = self.username_entry.get().strip()
        pwd = self.password_entry.get().strip()
        if not user or not pwd:
            messagebox.showwarning("Datos faltantes", "Completa todos los campos")
            return
        if agregar_usuario(user, pwd):
            messagebox.showinfo("Éxito", "Usuario agregado correctamente")
            self.limpiar_campos()
            self.cargar_usuarios()
        else:
            messagebox.showerror("Error", "No se pudo agregar el usuario")

    # Actualizar usuario (UPDATE)
    def actualizar(self):
        id_val = self.id_entry.get().strip()
        user = self.username_entry.get().strip()
        pwd = self.password_entry.get().strip()
        if not id_val or not user or not pwd:
            messagebox.showwarning("Datos faltantes", "Selecciona un usuario y completa los campos")
            return
        if actualizar_usuario(id_val, user, pwd):
            messagebox.showinfo("Éxito", "Usuario actualizado")
            self.limpiar_campos()
            self.cargar_usuarios()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el usuario")

    # Eliminar usuario (DELETE)
    def eliminar(self):
        id_val = self.id_entry.get().strip()
        if not id_val:
            messagebox.showwarning("Datos faltantes", "Selecciona un usuario para eliminar")
            return
        confirmar = messagebox.askyesno("Confirmar eliminación", "¿Seguro que deseas eliminar este usuario?")
        if not confirmar:
            return
        if eliminar_usuario(id_val):
            messagebox.showinfo("Éxito", "Usuario eliminado")
            self.limpiar_campos()
            self.cargar_usuarios()
        else:
            messagebox.showerror("Error", "No se pudo eliminar")

    # Al hacer clic en una fila de la tabla, pasar valores a los entries
    def seleccionar_fila(self, event):
        item = self.tabla.focus()
        if not item:
            return
        datos = self.tabla.item(item, "values")
        # datos = (ID, username, password)
        self.id_entry.delete(0, tk.END)
        self.id_entry.insert(0, datos[0])
        self.username_entry.delete(0, tk.END)
        self.username_entry.insert(0, datos[1])
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, datos[2])

    def limpiar_campos(self):
        self.id_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    # ---------- CERRAR SESIÓN ----------
    def cerrar_sesion(self):
        confirmar = messagebox.askyesno("Cerrar sesión", "¿Deseas cerrar sesión?")
        if not confirmar:
            return
        # Cerrar la ventana actual (dashboard)
        try:
            self.root.destroy()
        except Exception:
            pass

        # Volver al login: ejecutamos main nuevamente
        # IMPORTANTE: import local para evitar problemas circulares al importar al inicio
        try:
            import main
            main.main()
        except Exception as e:
            # Si por alguna razón no funciona volver a crear LoginApp directamente:
            from login_view import LoginApp
            new_root = tk.Tk()
            LoginApp(new_root)
            new_root.mainloop()
