import tkinter as tk
from tkinter import ttk, messagebox
from user_controlller import obtener_usuarios, agregar_usuario, actualizar_usuario, eliminar_usuario

class UserApp:
    def __init__(self, logged_user):
        self.logged_user = logged_user
        self.root = tk.Tk()
        self.root.title(f"Usuarios - Sesión: {logged_user}")
        self.root.geometry("700x450")
        self.root.resizable(False, False)
        self.create_widgets()
        self.cargar_usuarios()

    def create_widgets(self):
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(fill='both', expand=True)

        # Formulario
        form = tk.Frame(frame)
        form.pack(side='top', fill='x', pady=(0,10))

        tk.Label(form, text='ID:').grid(row=0, column=0, sticky='w')
        self.id_var = tk.StringVar()
        self.id_entry = tk.Entry(form, textvariable=self.id_var, state='readonly', width=10)
        self.id_entry.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(form, text='Usuario:').grid(row=0, column=2, sticky='w')
        self.usuario_var = tk.StringVar()
        self.usuario_entry = tk.Entry(form, textvariable=self.usuario_var, width=25)
        self.usuario_entry.grid(row=0, column=3, padx=5, pady=2)

        tk.Label(form, text='Contraseña:').grid(row=1, column=2, sticky='w')
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(form, textvariable=self.password_var, width=25, show='*')
        self.password_entry.grid(row=1, column=3, padx=5, pady=2)

        # Botones CRUD
        botones = tk.Frame(frame)
        botones.pack(fill='x', pady=(0,10))

        tk.Button(botones, text='Agregar', command=self.agregar_usuario).pack(side='left', padx=5)
        tk.Button(botones, text='Actualizar', command=self.actualizar_usuario).pack(side='left', padx=5)
        tk.Button(botones, text='Eliminar', command=self.eliminar_usuario).pack(side='left', padx=5)
        tk.Button(botones, text='Limpiar', command=self.limpiar_campos).pack(side='left', padx=5)

        # Treeview para mostrar usuarios
        columns = ('id','usuario','password')
        self.tree = ttk.Treeview(frame, columns=columns, show='headings', height=12)
        self.tree.heading('id', text='ID')
        self.tree.heading('usuario', text='Usuario')
        self.tree.heading('password', text='Contraseña')
        self.tree.column('id', width=60, anchor='center')
        self.tree.column('usuario', width=220, anchor='w')
        self.tree.column('password', width=220, anchor='w')
        self.tree.pack(fill='both', expand=True)

        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

    def cargar_usuarios(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        usuarios = obtener_usuarios()
        for u in usuarios:
            self.tree.insert('', 'end', values=u)

    def on_tree_select(self, event):
        sel = self.tree.selection()
        if not sel: return
        vals = self.tree.item(sel[0])['values']
        if vals:
            self.id_var.set(vals[0])
            self.usuario_var.set(vals[1])
            self.password_var.set(vals[2])

    def validar_campos(self):
        usuario = self.usuario_var.get().strip()
        password = self.password_var.get().strip()
        if not usuario or not password:
            messagebox.showerror("Validación", "Usuario y contraseña no pueden estar vacíos.")
            return False
        return True

    def agregar_usuario(self):
        if not self.validar_campos():
            return
        usuario = self.usuario_var.get().strip()
        password = self.password_var.get().strip()
        ok, msg = agregar_usuario(usuario, password)
        if ok:
            messagebox.showinfo("Éxito", msg)
            self.cargar_usuarios()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", msg)

    def actualizar_usuario(self):
        if not self.validar_campos():
            return
        id_val = self.id_var.get().strip()
        if not id_val:
            messagebox.showerror("Error", "Selecciona un usuario de la lista para actualizar.")
            return
        ok, msg = actualizar_usuario(int(id_val), self.usuario_var.get().strip(), self.password_var.get().strip())
        if ok:
            messagebox.showinfo("Éxito", msg)
            self.cargar_usuarios()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", msg)

    def eliminar_usuario(self):
        id_val = self.id_var.get().strip()
        if not id_val:
            messagebox.showerror("Error", "Selecciona un usuario de la lista para eliminar.")
            return
        if not messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar el usuario seleccionado?"):
            return
        ok, msg = eliminar_usuario(int(id_val))
        if ok:
            messagebox.showinfo("Éxito", msg)
            self.cargar_usuarios()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", msg)

    def limpiar_campos(self):
        self.id_var.set('')
        self.usuario_var.set('')
        self.password_var.set('')

    def run(self):
        self.root.mainloop()
