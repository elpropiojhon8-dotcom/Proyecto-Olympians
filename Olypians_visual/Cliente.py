import tkinter as tk
from tkinter import messagebox
import sqlite3
from pathlib import Path

from Formulario import crear_interfaz_registros
from Persona import Persona


RUTA_BASE_DATOS = Path(__file__).resolve().with_name("clientes.db")


def inicializar_base_datos():
    """Crea la tabla de clientes si todavía no existe."""
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    try:
        conexion.execute(
            """CREATE TABLE IF NOT EXISTS clientes (
                id_cliente TEXT PRIMARY KEY,
                nombres TEXT NOT NULL DEFAULT '',
                apellidos TEXT NOT NULL DEFAULT '',
                telefono TEXT NOT NULL DEFAULT '',
                fecha_ingreso TEXT NOT NULL DEFAULT '',
                estado TEXT NOT NULL DEFAULT 'Activo',
                peso TEXT NOT NULL DEFAULT ''
            )"""
        )
        conexion.commit()
    finally:
        conexion.close()


def cargar_clientes():
    """Lee los clientes guardados y devuelve una lista de objetos Cliente."""
    inicializar_base_datos()
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    try:
        filas = conexion.execute(
            """SELECT id_cliente, nombres, apellidos, telefono,
                      fecha_ingreso, estado, peso
               FROM clientes ORDER BY id_cliente"""
        ).fetchall()
    finally:
        conexion.close()
    return [
        Cliente(
            id_cliente=fila[0], nombres=fila[1], apellidos=fila[2],
            telefono=fila[3], fecha_ingreso=fila[4], estado=fila[5], peso=fila[6]
        )
        for fila in filas
    ]


def guardar_cliente(cliente):
    """Inserta un cliente en SQLite; el ID no se puede repetir."""
    inicializar_base_datos()
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    try:
        conexion.execute(
            """INSERT INTO clientes
               (id_cliente, nombres, apellidos, telefono, fecha_ingreso, estado, peso)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                cliente.id_cliente, cliente.nombres, cliente.apellidos,
                cliente.telefono, cliente.fecha_ingreso, cliente.estado, cliente.peso
            ),
        )
        conexion.commit()
    finally:
        conexion.close()


def eliminar_cliente(cliente):
    """Elimina de SQLite el cliente indicado."""
    inicializar_base_datos()
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    try:
        conexion.execute("DELETE FROM clientes WHERE id_cliente = ?", (cliente.id_cliente,))
        conexion.commit()
    finally:
        conexion.close()


class Cliente(Persona):
    def __init__(self, **datos):
        super().__init__(**datos)
        self.id_cliente = datos.get("id_cliente", datos.get("id", ""))
        self.id = self.id_cliente
        self.fecha_ingreso = datos.get("fecha_ingreso", "")
        self.estado = datos.get("estado", "Activo")
        self.peso = datos.get("peso", "")
        self.membresia = None

    def inscribirse(self, plan):
        self.membresia = plan

    def cancelar_membresia(self):
        self.membresia = None
        self.estado = "Inactivo"

    def actualizar_peso(self, peso):
        self.peso = float(peso)



    def get_id(self):
        return self.id_cliente

    def set_id(self, valor):
        self.id_cliente = valor
        self.id = valor

    def get_id_cliente(self):
        return self.id_cliente

    def set_id_cliente(self, valor):
        self.id_cliente = valor
        self.id = valor

    def get_fecha_ingreso(self):
        return self.fecha_ingreso

    def set_fecha_ingreso(self, valor):
        self.fecha_ingreso = valor

    def get_estado(self):
        return self.estado

    def set_estado(self, valor):
        self.estado = valor

    def get_peso(self):
        return self.peso

    def set_peso(self, valor):
        self.peso = valor

    def get_membresia(self):
        return self.membresia

    def set_membresia(self, valor):
        self.membresia = valor
def crear_interfaz(parent, clientes, planes=None):
    campos = [("id_cliente", "ID cliente"), ("nombres", "Nombres"), ("apellidos", "Apellidos"),
              ("telefono", "Teléfono"), ("fecha_ingreso", "Fecha de ingreso"), ("estado", "Estado"), ("peso", "Peso")]
    crear_interfaz_registros(
        parent, clientes, Cliente, campos, "Registro de clientes",
        cargar_registros=cargar_clientes,
        guardar_registro=guardar_cliente,
        eliminar_registro=eliminar_cliente,
    )
