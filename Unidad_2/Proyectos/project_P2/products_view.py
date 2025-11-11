import tkinter as tk
from tkinter import ttk, messagebox
from products_controller import obtener_productos, agregar_producto, actualizar_producto, eliminar_producto

class ProductApp:
    def __init__(self, logged_user):
        self.logged_user = logged_user
        self.root = tk.Tk()
        self.root.title(f"Gestión de Productos - Sesión: {logged_user}")
        self.root.geometry("950x550")
        self.root.resizable(True, True)
        self.crear_elementos()
        self.cargar_productos()

    def crear_elementos(self):
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        # Formulario
        form = tk.Frame(frame)
        form.pack(side="top", fill="x", pady=(0,10))

        labels = ["ID:", "Nombre:", "Descripción:", "Stock:", "Precio:", "Status:", "Marca:", "Proveedor:"]
        self.vars = {label: tk.StringVar() for label in labels}
        
        entries = [
            ("ID:", 0, 0, 10, True),
            ("Nombre:", 0, 2, 25, False),
            ("Descripción:", 1, 0, 30, False),
            ("Stock:", 1, 2, 10, False),
            ("Precio:", 2, 0, 10, False),
            ("Status:", 2, 2, 15, False),
            ("Marca:", 3, 0, 20, False),
            ("Proveedor:", 3, 2, 20, False)
        ]

        for label, row, col, width, readonly in entries:
            tk.Label(form, text=label).grid(row=row, column=col, sticky="w", padx=5, pady=3)
            entry = tk.Entry(form, textvariable=self.vars[label], width=width)
            if readonly:
                entry.config(state="readonly")
            entry.grid(row=row, column=col+1, padx=5, pady=3)

        # Botones
        botones = tk.Frame(frame)
        botones.pack(fill="x", pady=(0,10))
        tk.Button(botones, text="Agregar", command=self.agregar_producto).pack(side="left", padx=5)
        tk.Button(botones, text="Actualizar", command=self.actualizar_producto).pack(side="left", padx=5)
        tk.Button(botones, text="Eliminar", command=self.eliminar_producto).pack(side="left", padx=5)
        tk.Button(botones, text="Limpiar", command=self.limpiar_campos).pack(side="left", padx=5)

        # Tabla
        cols = ["ID", "Nombre", "Descripción", "Stock", "Precio", "Status", "Marca", "Proveedor"]
        self.tree = ttk.Treeview(frame, columns=cols, show="headings", height=12)
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_producto)

    def cargar_productos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        productos = obtener_productos()
        for p in productos:
            self.tree.insert("", "end", values=p)

    def seleccionar_producto(self, event):
        seleccion = self.tree.selection()
        if not seleccion: return
        valores = self.tree.item(seleccion[0])["values"]
        labels = ["ID:", "Nombre:", "Descripción:", "Stock:", "Precio:", "Status:", "Marca:", "Proveedor:"]
        for i, label in enumerate(labels):
            self.vars[label].set(valores[i])

    def validar_campos(self):
        if not self.vars["Nombre:"].get().strip() or not self.vars["Precio:"].get().strip():
            messagebox.showerror("Error de validación", "El nombre y precio del producto son obligatorios.")
            return False
        return True

    def agregar_producto(self):
        if not self.validar_campos(): return
        nombre = self.vars["Nombre:"].get().strip()
        descripcion = self.vars["Descripción:"].get().strip()
        stock = self.vars["Stock:"].get().strip() or 0
        precio = self.vars["Precio:"].get().strip() or 0
        status = self.vars["Status:"].get().strip() or "Disponible"
        marca = self.vars["Marca:"].get().strip()
        proveedor = self.vars["Proveedor:"].get().strip()
        ok, msg = agregar_producto(nombre, descripcion, stock, precio, status, marca, proveedor)
        if ok:
            messagebox.showinfo("Éxito", msg)
            self.cargar_productos()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", msg)

    def actualizar_producto(self):
        if not self.validar_campos(): return
        id_producto = self.vars["ID:"].get().strip()
        if not id_producto:
            messagebox.showerror("Error", "Selecciona un producto de la lista.")
            return
        nombre = self.vars["Nombre:"].get().strip()
        descripcion = self.vars["Descripción:"].get().strip()
        stock = self.vars["Stock:"].get().strip() or 0
        precio = self.vars["Precio:"].get().strip() or 0
        status = self.vars["Status:"].get().strip()
        marca = self.vars["Marca:"].get().strip()
        proveedor = self.vars["Proveedor:"].get().strip()
        ok, msg = actualizar_producto(id_producto, nombre, descripcion, stock, precio, status, marca, proveedor)
        if ok:
            messagebox.showinfo("Éxito", msg)
            self.cargar_productos()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", msg)

    def eliminar_producto(self):
        id_producto = self.vars["ID:"].get().strip()
        if not id_producto:
            messagebox.showerror("Error", "Selecciona un producto de la lista.")
            return
        if not messagebox.askyesno("Confirmar", "¿Deseas eliminar este producto?"):
            return
        ok, msg = eliminar_producto(id_producto)
        if ok:
            messagebox.showinfo("Éxito", msg)
            self.cargar_productos()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", msg)

    def limpiar_campos(self):
        for v in self.vars.values():
            v.set("")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ProductApp("admin")
    app.run()
