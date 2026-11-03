import tkinter as tk
from tkinter import messagebox

from Formulario import crear_interfaz_registros
from Persona import Persona


class Cliente(Persona):
    def __init__(self, **datos):
        super().__init__(**datos)
        self.id = datos.get("id_cliente", datos.get("id", ""))
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


def crear_interfaz(parent, clientes, planes=None):
    campos = [("id_cliente", "ID cliente"), ("nombres", "Nombres"), ("apellidos", "Apellidos"),
              ("telefono", "Teléfono"), ("fecha_ingreso", "Fecha de ingreso"), ("estado", "Estado"), ("peso", "Peso")]
    crear_interfaz_registros(parent, clientes, Cliente, campos, "Registro de clientes")
