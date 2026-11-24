import tkinter as tk
from tkinter import messagebox, ttk
import json
import sqlite3
from pathlib import Path


RUTA_BASE_DATOS = Path(__file__).resolve().with_name("clientes.db")


def _inicializar_registros_generales():
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    try:
        conexion.execute(
            """CREATE TABLE IF NOT EXISTS registros_generales (
                tipo TEXT NOT NULL,
                id_registro TEXT NOT NULL,
                datos TEXT NOT NULL,
                PRIMARY KEY (tipo, id_registro)
            )"""
        )
        conexion.commit()
    finally:
        conexion.close()


def _cargar_registros_generales(clase):
    _inicializar_registros_generales()
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    try:
        filas = conexion.execute(
            "SELECT datos FROM registros_generales WHERE tipo = ? ORDER BY id_registro",
            (clase.__name__,),
        ).fetchall()
    finally:
        conexion.close()
    return [clase(**json.loads(fila[0])) for fila in filas]


def _guardar_registro_general(clase, campos, objeto):
    _inicializar_registros_generales()
    datos = {campo: getattr(objeto, campo, "") for campo, _ in campos}
    id_registro = str(datos.get(campos[0][0], ""))
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    try:
        conexion.execute(
            "INSERT INTO registros_generales (tipo, id_registro, datos) VALUES (?, ?, ?)",
            (clase.__name__, id_registro, json.dumps(datos, ensure_ascii=False)),
        )
        conexion.commit()
    finally:
        conexion.close()


def _eliminar_registro_general(clase, campos, objeto):
    _inicializar_registros_generales()
    id_registro = str(getattr(objeto, campos[0][0], ""))
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    try:
        conexion.execute(
            "DELETE FROM registros_generales WHERE tipo = ? AND id_registro = ?",
            (clase.__name__, id_registro),
        )
        conexion.commit()
    finally:
        conexion.close()


def crear_interfaz_registros(
    parent, registros, clase, campos, titulo,
    cargar_registros=None, guardar_registro=None, eliminar_registro=None,
):
    """Crea un formulario sencillo y una tabla para una clase del gimnasio."""
    if cargar_registros is None:
        cargar_registros = lambda: _cargar_registros_generales(clase)
    if guardar_registro is None:
        guardar_registro = lambda objeto: _guardar_registro_general(clase, campos, objeto)
    if eliminar_registro is None:
        eliminar_registro = lambda objeto: _eliminar_registro_general(clase, campos, objeto)

    contenido = ttk.Frame(parent, style="Page.TFrame", padding=(18, 15, 18, 14))
    contenido.pack(fill="both", expand=True)

    ttk.Label(contenido, text=titulo, style="Section.TLabel").pack(anchor="w", pady=(0, 2))
    ttk.Label(
        contenido,
        text="Complete los campos para agregar un registro a esta sección.",
        style="PageHint.TLabel",
    ).pack(anchor="w", pady=(0, 12))

    tarjeta_formulario = ttk.Frame(contenido, style="Card.TFrame", padding=(16, 13, 16, 12))
    tarjeta_formulario.pack(fill="x")
    ttk.Label(tarjeta_formulario, text="Información", style="CardTitle.TLabel").pack(anchor="w")
    ttk.Label(
        tarjeta_formulario,
        text="Los datos se guardan al pulsar el botón verde.",
        style="CardHint.TLabel",
    ).pack(anchor="w", pady=(2, 9))

    marco = ttk.Frame(tarjeta_formulario, style="CardInner.TFrame")
    marco.pack(fill="x")
    entradas = {}

    for indice, (atributo, etiqueta) in enumerate(campos):
        fila, pareja = divmod(indice, 2)
        columna_etiqueta = pareja * 2
        columna_entrada = columna_etiqueta + 1
        ttk.Label(marco, text=etiqueta, style="Field.TLabel").grid(
            row=fila * 2, column=columna_etiqueta, sticky="w", padx=(5, 9), pady=(5, 2)
        )
        entrada = ttk.Entry(marco, width=24)
        entrada.grid(row=fila * 2 + 1, column=columna_entrada, sticky="ew", padx=(0, 17), pady=(0, 5))
        entradas[atributo] = entrada
    marco.columnconfigure(1, weight=1, uniform="campo")
    marco.columnconfigure(3, weight=1, uniform="campo")

    botones = ttk.Frame(tarjeta_formulario, style="CardInner.TFrame", padding=(0, 10, 0, 0))
    botones.pack(fill="x")
    ttk.Button(botones, text="Guardar registro", style="Primary.TButton", command=lambda: guardar()).pack(
        side="left", padx=(0, 7)
    )
    ttk.Button(botones, text="Eliminar seleccionado", style="Danger.TButton", command=lambda: eliminar()).pack(
        side="left"
    )

    tarjeta_tabla = ttk.Frame(contenido, style="Card.TFrame", padding=10)
    tarjeta_tabla.pack(fill="both", expand=True, pady=(12, 0))
    encabezado_tabla = ttk.Frame(tarjeta_tabla, style="CardInner.TFrame")
    encabezado_tabla.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 7))
    ttk.Label(encabezado_tabla, text="Registros guardados", style="CardTitle.TLabel").pack(side="left")
    contador = ttk.Label(encabezado_tabla, text="0 registros", style="Count.TLabel")
    contador.pack(side="right")

    tabla = ttk.Treeview(tarjeta_tabla, columns=[campo for campo, _ in campos], show="headings", height=9)
    for atributo, etiqueta in campos:
        tabla.heading(atributo, text=etiqueta)
        tabla.column(atributo, width=125, minwidth=85, anchor="center")
    barra_y = ttk.Scrollbar(tarjeta_tabla, orient="vertical", command=tabla.yview)
    barra_x = ttk.Scrollbar(tarjeta_tabla, orient="horizontal", command=tabla.xview)
    tabla.configure(yscrollcommand=barra_y.set, xscrollcommand=barra_x.set)
    tabla.tag_configure("fila_alterna", background="#F4F8FC")
    barra_y.configure(command=tabla.yview)
    barra_x.configure(command=tabla.xview)
    tabla.grid(row=1, column=0, sticky="nsew")
    barra_y.grid(row=1, column=1, sticky="ns", padx=(5, 0))
    barra_x.grid(row=2, column=0, sticky="ew", pady=(5, 0))
    tarjeta_tabla.rowconfigure(1, weight=1)
    tarjeta_tabla.columnconfigure(0, weight=1)

    def refrescar():
        tabla.delete(*tabla.get_children())
        for indice, objeto in enumerate(registros):
            etiquetas_fila = ("fila_alterna",) if indice % 2 else ()
            tabla.insert(
                "", "end",
                values=[getattr(objeto, campo, "") for campo, _ in campos],
                tags=etiquetas_fila,
            )
        contador.configure(text=f"{len(registros)} registros")

    def guardar():
        valores = {campo: entrada.get().strip() for campo, entrada in entradas.items()}
        if not valores.get(campos[0][0]):
            messagebox.showwarning("Falta el identificador", "Escribe el ID para guardar el registro.", parent=parent)
            return
        if any(str(getattr(objeto, campos[0][0], "")) == valores[campos[0][0]] for objeto in registros):
            messagebox.showwarning("ID repetido", "Ya existe un registro con ese ID.", parent=parent)
            return
        objeto = clase(**valores)
        if guardar_registro is not None:
            try:
                guardar_registro(objeto)
            except Exception as error:
                messagebox.showerror(
                    "No se pudo guardar",
                    f"El registro no se guardó en el almacenamiento permanente.\n{error}",
                    parent=parent,
                )
                return
        registros.append(objeto)
        for entrada in entradas.values():
            entrada.delete(0, tk.END)
        refrescar()

    def eliminar():
        seleccion = tabla.selection()
        if not seleccion:
            messagebox.showinfo("Selecciona un registro", "Elige una fila de la tabla para eliminarla.", parent=parent)
            return
        indice = tabla.index(seleccion[0])
        objeto = registros[indice]
        if eliminar_registro is not None:
            try:
                eliminar_registro(objeto)
            except Exception as error:
                messagebox.showerror(
                    "No se pudo eliminar",
                    f"El registro sigue guardado.\n{error}",
                    parent=parent,
                )
                return
        registros.pop(indice)
        refrescar()

    if cargar_registros is not None:
        try:
            registros[:] = cargar_registros()
        except Exception as error:
            messagebox.showerror(
                "No se pudieron cargar los clientes",
                f"No fue posible leer los registros guardados.\n{error}",
                parent=parent,
            )
    refrescar()
