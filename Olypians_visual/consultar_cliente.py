"""Consulta un cliente y sus registros relacionados en la base local."""

import json
import sqlite3
from pathlib import Path


RUTA_BASE_DATOS = Path(__file__).resolve().with_name("clientes.db")

ETIQUETAS = {
    "id_cliente": "ID del cliente",
    "id_membresia": "ID de membresía",
    "id_plan": "ID del plan",
    "id_plan_nutricional": "ID del plan nutricional",
    "id_nutricionista": "ID del nutricionista",
    "id_producto": "ID del producto",
    "id_pago": "ID del pago",
    "id_rutina": "ID de la rutina",
    "id_asistencia": "ID de asistencia",
    "fecha_ingreso": "Fecha de ingreso",
    "fecha_inicio": "Fecha de inicio",
    "fecha_fin": "Fecha de fin",
    "fecha_creacion": "Fecha de creación",
    "hora_entrada": "Hora de entrada",
    "hora_salida": "Hora de salida",
    "nombres": "Nombres",
    "apellidos": "Apellidos",
    "telefono": "Teléfono",
    "estado": "Estado",
    "peso": "Peso",
    "nombre": "Nombre",
    "objetivo": "Objetivo",
    "nivel": "Nivel",
    "calorias": "Calorías",
    "proteinas": "Proteínas",
    "valor": "Valor",
    "metodo": "Método de pago",
    "cantidad": "Cantidad",
    "total": "Total",
    "precio": "Precio",
    "duracion": "Duración",
    "tipo": "Tipo",
    "series": "Series",
    "repeticiones": "Repeticiones",
    "dia": "Día",
    "hora_inicio": "Hora de inicio",
    "hora_fin": "Hora de fin",
    "descripcion": "Descripción",
    "costo": "Costo",
    "capacidad": "Capacidad",
    "id_horario": "ID del horario",
    "stock": "Existencias",
    "especialidad": "Especialidad",
    "salario": "Salario",
    "turno": "Turno",
    "usuario": "Usuario",
    "contrasena": "Contraseña",
}

NOMBRES_TIPO = {
    "Membresia": "Membresías",
    "Pago": "Pagos",
    "Rutina": "Rutinas de ejercicio",
    "Asistencia": "Asistencias",
    "PlanNutricional": "Planes nutricionales",
    "Venta": "Ventas",
}


def abrir_base_datos():
    """Abre la base existente y muestra un mensaje claro si aún no existe."""
    if not RUTA_BASE_DATOS.exists():
        print("Todavía no hay una base de datos. Abre primero la aplicación y registra un cliente.")
        return None
    return sqlite3.connect(RUTA_BASE_DATOS)


def buscar_registro(conexion, tipo, campo_id, valor_id):
    """Busca un objeto guardado por su tipo e identificador."""
    existe_tabla = conexion.execute(
        "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'registros_generales'"
    ).fetchone()
    if not existe_tabla:
        return None
    filas = conexion.execute(
        "SELECT datos FROM registros_generales WHERE tipo = ?",
        (tipo,),
    ).fetchall()
    for (texto_datos,) in filas:
        datos = json.loads(texto_datos)
        if str(datos.get(campo_id, "")) == str(valor_id):
            return datos
    return None


def imprimir_datos(titulo, datos, sangria="  "):
    print(f"\n{titulo}")
    for campo, valor in datos.items():
        etiqueta = ETIQUETAS.get(campo, campo.replace("_", " ").capitalize())
        print(f"{sangria}{etiqueta}: {valor if valor not in (None, '') else '(sin dato)'}")


def consultar_cliente(id_cliente):
    conexion = abrir_base_datos()
    if conexion is None:
        return

    try:
        tablas = {
            fila[0]
            for fila in conexion.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            ).fetchall()
        }
        if "clientes" not in tablas:
            print("La base de datos todavía no contiene la tabla de clientes.")
            return

        fila = conexion.execute(
            """SELECT id_cliente, nombres, apellidos, telefono,
                      fecha_ingreso, estado, peso
               FROM clientes WHERE id_cliente = ?""",
            (id_cliente,),
        ).fetchone()
        if fila is None:
            print(f"No se encontró ningún cliente con el ID {id_cliente}.")
            return

        cliente = dict(zip(
            ("id_cliente", "nombres", "apellidos", "telefono", "fecha_ingreso", "estado", "peso"),
            fila,
        ))
        imprimir_datos("DATOS DEL CLIENTE", cliente)

        relacionados = []
        if "registros_generales" in tablas:
            for tipo, texto_datos in conexion.execute(
                "SELECT tipo, datos FROM registros_generales ORDER BY tipo"
            ).fetchall():
                datos = json.loads(texto_datos)
                if str(datos.get("id_cliente", "")) == str(id_cliente):
                    relacionados.append((tipo, datos))

        if not relacionados:
            print("\nNo hay membresías, pagos, rutinas, asistencias, ventas ni planes nutricionales guardados para este cliente.")
            return

        print("\nREGISTROS RELACIONADOS")
        for tipo, datos in relacionados:
            titulo = NOMBRES_TIPO.get(tipo, tipo)
            imprimir_datos(titulo, datos)

            if tipo == "Membresia" and datos.get("id_plan"):
                plan = buscar_registro(conexion, "Plan", "id_plan", datos["id_plan"])
                if plan:
                    imprimir_datos("Plan asociado", plan, sangria="    ")
                else:
                    print("    Plan asociado: no se encontró el ID en los planes guardados.")

            if tipo == "Venta" and datos.get("id_producto"):
                producto = buscar_registro(conexion, "Producto", "id_producto", datos["id_producto"])
                if producto:
                    imprimir_datos("Producto vendido", producto, sangria="    ")

            if tipo == "PlanNutricional" and datos.get("id_nutricionista"):
                nutricionista = buscar_registro(
                    conexion, "Nutricionista", "id_nutricionista", datos["id_nutricionista"]
                )
                if nutricionista:
                    imprimir_datos("Nutricionista asociado", nutricionista, sangria="    ")
    finally:
        conexion.close()


def main():
    id_cliente = input("Escribe el ID del cliente que quieres consultar: ").strip()
    if not id_cliente:
        print("Debes escribir un ID de cliente.")
        return
    consultar_cliente(id_cliente)


if __name__ == "__main__":
    main()
