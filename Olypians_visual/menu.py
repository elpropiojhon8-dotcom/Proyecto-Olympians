"""Menú alternativo de Olympians para usar desde la consola."""

from Persona import Persona
from Cliente import Cliente
from Entrenador import Entrenador
from Administrador import Administrador
from Recepcionista import Recepcionista
from Plan import Plan
from Membresia import Membresia
from Pago import Pago
from Rutina import Rutina
from Ejercicio import Ejercicio
from Maquina import Maquina
from Mantenimiento import Mantenimiento
from ClaseGrupal import ClaseGrupal
from Horario import Horario
from Asistencia import Asistencia
from Nutricionista import Nutricionista
from PlanNutricional import PlanNutricional
from Alimento import Alimento
from Producto import Producto
from Venta import Venta


SECCIONES = [
    ("Personas", Persona, [("id", "ID"), ("nombres", "Nombres"), ("apellidos", "Apellidos"), ("telefono", "Teléfono")]),
    ("Clientes", Cliente, [("id_cliente", "ID cliente"), ("nombres", "Nombres"), ("apellidos", "Apellidos"), ("telefono", "Teléfono"), ("fecha_ingreso", "Fecha de ingreso"), ("estado", "Estado"), ("peso", "Peso")]),
    ("Entrenadores", Entrenador, [("id_entrenador", "ID entrenador"), ("nombres", "Nombres"), ("apellidos", "Apellidos"), ("telefono", "Teléfono"), ("especialidad", "Especialidad"), ("salario", "Salario")]),
    ("Administradores", Administrador, [("id_administrador", "ID administrador"), ("nombres", "Nombres"), ("apellidos", "Apellidos"), ("telefono", "Teléfono"), ("usuario", "Usuario"), ("contrasena", "Contraseña")]),
    ("Recepcionistas", Recepcionista, [("id_recepcionista", "ID recepcionista"), ("nombres", "Nombres"), ("apellidos", "Apellidos"), ("telefono", "Teléfono"), ("turno", "Turno"), ("salario", "Salario")]),
    ("Planes", Plan, [("id_plan", "ID plan"), ("nombre", "Nombre"), ("precio", "Precio"), ("duracion", "Duración en días")]),
    ("Membresías", Membresia, [("id_membresia", "ID membresía"), ("id_cliente", "ID cliente"), ("id_plan", "ID plan"), ("fecha_inicio", "Fecha de inicio"), ("fecha_fin", "Fecha de fin"), ("estado", "Estado")]),
    ("Pagos", Pago, [("id_pago", "ID pago"), ("id_cliente", "ID cliente"), ("fecha", "Fecha"), ("valor", "Valor"), ("metodo", "Método")]),
    ("Rutinas", Rutina, [("id_rutina", "ID rutina"), ("id_cliente", "ID cliente"), ("nombre", "Nombre"), ("nivel", "Nivel"), ("objetivo", "Objetivo")]),
    ("Ejercicios", Ejercicio, [("id_ejercicio", "ID ejercicio"), ("nombre", "Nombre"), ("series", "Series"), ("repeticiones", "Repeticiones")]),
    ("Máquinas", Maquina, [("id_maquina", "ID máquina"), ("nombre", "Nombre"), ("tipo", "Tipo"), ("estado", "Estado")]),
    ("Mantenimientos", Mantenimiento, [("id_mantenimiento", "ID mantenimiento"), ("id_maquina", "ID máquina"), ("fecha", "Fecha"), ("descripcion", "Descripción"), ("costo", "Costo")]),
    ("Clases grupales", ClaseGrupal, [("id_clase", "ID clase"), ("nombre", "Nombre"), ("capacidad", "Capacidad"), ("id_horario", "ID horario")]),
    ("Horarios", Horario, [("id_horario", "ID horario"), ("dia", "Día"), ("hora_inicio", "Hora de inicio"), ("hora_fin", "Hora de fin")]),
    ("Asistencias", Asistencia, [("id_asistencia", "ID asistencia"), ("id_cliente", "ID cliente"), ("fecha", "Fecha"), ("hora_entrada", "Hora de entrada"), ("hora_salida", "Hora de salida")]),
    ("Nutricionistas", Nutricionista, [("id_nutricionista", "ID nutricionista"), ("nombres", "Nombres"), ("apellidos", "Apellidos"), ("telefono", "Teléfono"), ("especialidad", "Especialidad"), ("salario", "Salario")]),
    ("Planes nutricionales", PlanNutricional, [("id_plan_nutricional", "ID plan nutricional"), ("id_cliente", "ID cliente"), ("id_nutricionista", "ID nutricionista"), ("objetivo", "Objetivo"), ("calorias", "Calorías"), ("fecha_creacion", "Fecha de creación")]),
    ("Alimentos", Alimento, [("id_alimento", "ID alimento"), ("nombre", "Nombre"), ("calorias", "Calorías"), ("proteinas", "Proteínas")]),
    ("Productos", Producto, [("id_producto", "ID producto"), ("nombre", "Nombre"), ("precio", "Precio"), ("stock", "Stock")]),
    ("Ventas", Venta, [("id_venta", "ID venta"), ("id_producto", "ID producto"), ("id_cliente", "ID cliente"), ("fecha", "Fecha"), ("cantidad", "Cantidad"), ("total", "Total")]),
]

registros = {nombre: [] for nombre, _clase, _campos in SECCIONES}


def mostrar_registros(nombre, campos):
    datos = registros[nombre]
    if not datos:
        print("\nTodavía no hay registros en esta sección.")
        return
    print(f"\n--- {nombre} ---")
    for numero, objeto in enumerate(datos, start=1):
        resumen = " | ".join(f"{etiqueta}: {getattr(objeto, atributo, '')}" for atributo, etiqueta in campos)
        print(f"{numero}. {resumen}")


def agregar_registro(nombre, clase, campos):
    valores = {}
    for atributo, etiqueta in campos:
        valores[atributo] = input(f"{etiqueta}: ").strip()

    campo_id = campos[0][0]
    if not valores[campo_id]:
        print("El ID es obligatorio; no se guardó el registro.")
        return
    if any(str(getattr(objeto, campo_id, "")) == valores[campo_id] for objeto in registros[nombre]):
        print("Ya existe un registro con ese ID.")
        return

    registros[nombre].append(clase(**valores))
    print("Registro guardado.")


def menu_seccion(nombre, clase, campos):
    while True:
        print(f"\n=== {nombre} ===")
        print("1. Registrar")
        print("2. Listar")
        print("0. Volver al menú principal")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            agregar_registro(nombre, clase, campos)
        elif opcion == "2":
            mostrar_registros(nombre, campos)
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


def main():
    while True:
        print("\n========== OLYMPIANS ==========")
        for numero, (nombre, _clase, _campos) in enumerate(SECCIONES, start=1):
            print(f"{numero}. {nombre}")
        print("0. Salir")
        opcion = input("Selecciona una sección: ").strip()
        if opcion == "0":
            print("Hasta luego.")
            break
        if not opcion.isdigit() or not 1 <= int(opcion) <= len(SECCIONES):
            print("Opción no válida. Intenta de nuevo.")
            continue
        nombre, clase, campos = SECCIONES[int(opcion) - 1]
        menu_seccion(nombre, clase, campos)


if __name__ == "__main__":
    main()
