import tkinter as tk
from tkinter import ttk

from Persona import crear_interfaz as interfaz_persona
from Cliente import crear_interfaz as interfaz_cliente
from Entrenador import crear_interfaz as interfaz_entrenador
from Administrador import crear_interfaz as interfaz_administrador
from Recepcionista import crear_interfaz as interfaz_recepcionista
from Plan import crear_interfaz as interfaz_plan
from Membresia import crear_interfaz as interfaz_membresia
from Pago import crear_interfaz as interfaz_pago
from Rutina import crear_interfaz as interfaz_rutina
from Ejercicio import crear_interfaz as interfaz_ejercicio
from Maquina import crear_interfaz as interfaz_maquina
from Mantenimiento import crear_interfaz as interfaz_mantenimiento
from ClaseGrupal import crear_interfaz as interfaz_clase_grupal
from Horario import crear_interfaz as interfaz_horario
from Asistencia import crear_interfaz as interfaz_asistencia
from Nutricionista import crear_interfaz as interfaz_nutricionista
from PlanNutricional import crear_interfaz as interfaz_plan_nutricional
from Alimento import crear_interfaz as interfaz_alimento
from Producto import crear_interfaz as interfaz_producto
from Venta import crear_interfaz as interfaz_venta


personas = []
clientes = []
entrenadores = []
administradores = []
recepcionistas = []
planes = []
membresias = []
pagos = []
rutinas = []
ejercicios = []
maquinas = []
mantenimientos = []
clases_grupales = []
horarios = []
asistencias = []
nutricionistas = []
planes_nutricionales = []
alimentos = []
productos = []
ventas = []


ventana = tk.Tk()
ventana.title("Olympians | Gestión del gimnasio")
ventana.geometry("1100x720")
ventana.minsize(850, 580)
ventana.configure(bg="#EAF2FB")

estilo = ttk.Style(ventana)
estilo.theme_use("clam")
estilo.configure(".", font=("Segoe UI", 10))
estilo.configure("TFrame", background="#EAF2FB")
estilo.configure("TLabel", background="#EAF2FB", foreground="#374151")
estilo.configure("Page.TFrame", background="#EAF2FB")
estilo.configure("PageHint.TLabel", background="#EAF2FB", foreground="#7C8A9C",
                  font=("Segoe UI", 9))
estilo.configure("Header.TFrame", background="#DCE9F7")
estilo.configure("Brand.TLabel", background="#DCE9F7", foreground="#334155",
                  font=("Segoe UI", 21, "bold"))
estilo.configure("Subtitle.TLabel", background="#DCE9F7", foreground="#64748B",
                  font=("Segoe UI", 10))
estilo.configure("Section.TLabel", background="#EAF2FB", foreground="#334155",
                  font=("Segoe UI", 15, "bold"))
estilo.configure("Field.TLabel", background="#FFFFFF", foreground="#687386",
                  font=("Segoe UI", 9, "bold"))
estilo.configure("CardTitle.TLabel", background="#FFFFFF", foreground="#4F5365",
                  font=("Segoe UI", 10, "bold"))
estilo.configure("CardHint.TLabel", background="#FFFFFF", foreground="#9199A5",
                  font=("Segoe UI", 8))
estilo.configure("Count.TLabel", background="#E7EFF9", foreground="#5B6F87",
                  padding=(9, 4), font=("Segoe UI", 8, "bold"))
estilo.configure("CardInner.TFrame", background="#FFFFFF")
estilo.configure("Card.TFrame", background="#FFFFFF", relief="solid",
                  borderwidth=1, lightcolor="#E7E4EF", darkcolor="#E7E4EF")
estilo.configure("Accent.TFrame", background="#AFCBE8")
estilo.configure("TNotebook", background="#EAF2FB", borderwidth=0,
                  tabmargins=(5, 5, 5, 0))
estilo.configure("TNotebook.Tab", background="#E2EBF5", foreground="#64748B",
                  padding=(13, 9), font=("Segoe UI", 9, "bold"))
estilo.map("TNotebook.Tab",
           background=[("selected", "#D7E8F8"), ("active", "#DCE9F7")],
           foreground=[("selected", "#36536F"), ("active", "#435A72")])
estilo.configure("TEntry", padding=7, fieldbackground="#FFFFFF",
                  foreground="#374151")
estilo.configure("TButton", padding=(12, 8), font=("Segoe UI", 9, "bold"),
                  background="#EEEAF5", foreground="#4F5365")
estilo.map("TButton", background=[("active", "#E3DFEF")])
estilo.configure("Primary.TButton", background="#DDEFE7", foreground="#365248")
estilo.map("Primary.TButton",
           background=[("pressed", "#C7E3D5"), ("active", "#CFE8DA")],
           foreground=[("active", "#365248")])
estilo.configure("Danger.TButton", background="#F5E3E7", foreground="#805B64")
estilo.map("Danger.TButton",
           background=[("pressed", "#ECD2D8"), ("active", "#F0D9DE")],
           foreground=[("active", "#805B64")])
estilo.configure("Treeview", background="#FFFFFF", fieldbackground="#FFFFFF",
                  foreground="#374151", rowheight=30, borderwidth=0,
                  font=("Segoe UI", 9))
estilo.configure("Treeview.Heading", background="#DCE9F7", foreground="#435A72",
                  padding=(8, 9), font=("Segoe UI", 9, "bold"))
estilo.map("Treeview", background=[("selected", "#D7E8F8")],
           foreground=[("selected", "#36536F")])

encabezado = ttk.Frame(ventana, style="Header.TFrame", padding=(18, 14))
encabezado.pack(fill="x")
ttk.Label(encabezado, text="OLYMPIANS", style="Brand.TLabel").pack(anchor="w")
ttk.Label(encabezado, text="GESTIÓN DEL GIMNASIO", style="Subtitle.TLabel").pack(anchor="w")
ttk.Frame(ventana, style="Accent.TFrame", height=4).pack(fill="x")

pestanas = ttk.Notebook(ventana)
pestanas.pack(fill="both", expand=True, padx=10, pady=(0, 10))

secciones = [
    ("Persona", interfaz_persona, personas),
    ("Cliente", interfaz_cliente, clientes),
    ("Entrenador", interfaz_entrenador, entrenadores),
    ("Administrador", interfaz_administrador, administradores),
    ("Recepcionista", interfaz_recepcionista, recepcionistas),
    ("Plan", interfaz_plan, planes),
    ("Membresía", interfaz_membresia, membresias),
    ("Pago", interfaz_pago, pagos),
    ("Rutina", interfaz_rutina, rutinas),
    ("Ejercicio", interfaz_ejercicio, ejercicios),
    ("Máquina", interfaz_maquina, maquinas),
    ("Mantenimiento", interfaz_mantenimiento, mantenimientos),
    ("Clase grupal", interfaz_clase_grupal, clases_grupales),
    ("Horario", interfaz_horario, horarios),
    ("Asistencia", interfaz_asistencia, asistencias),
    ("Nutricionista", interfaz_nutricionista, nutricionistas),
    ("Plan nutricional", interfaz_plan_nutricional, planes_nutricionales),
    ("Alimento", interfaz_alimento, alimentos),
    ("Producto", interfaz_producto, productos),
    ("Venta", interfaz_venta, ventas),
]

for nombre, crear_interfaz, registros in secciones:
    pagina = ttk.Frame(pestanas)
    pestanas.add(pagina, text=nombre)
    crear_interfaz(pagina, registros)

ventana.mainloop()
