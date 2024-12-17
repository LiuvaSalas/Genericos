from datetime import datetime


def registrar_transporte(transporte_data, punto_origen, cantidad, operario, fecha_hora):
    """
    Registra un nuevo transporte de carbón en la lista de transportes.

    Parámetros:
    - transporte_data (list): Lista que almacena los registros de transporte.
    - punto_origen (str): Nombre del punto de origen del carbón.
    - cantidad (int): Cantidad de carbón transportada.
    - operario (str): Nombre del operario encargado del transporte.
    - fecha_hora (str): Fecha y hora del transporte en formato 'YYYY-mm-dd HH:MM'.
    """

    nuevo_registro = {
        "PuntoOrigen": punto_origen,
        "Cantidad": cantidad,
        "Operario": operario,
        "FechaHora": datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M"),
    }
    transporte_data.append(nuevo_registro)


def analisis_por_operario(transporte_data, operario, fecha_inicio, fecha_fin):
    """
    Registra las caracteristicas del transporte por cada operario


    Parámetros:
    - transporte_data (list): Lista que almacena los registros de transporte.
    - operario (str): Nombre del operario encargado del transporte.
    - fecha_inicio(str): Fecha de inicio analisis por operario en formato YYYY-mm-dd.
    - fecha_fin(str): Nombre del operario encargado del transporte en formato YYYY-mm-dd.
    Retorna:
    - total(int): La cantidad total de carbon transportada por el operario del punto de origen segun las fechas de inicio y final
    """
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    total = 0
    for registro in transporte_data:
        if (
            registro["Operario"] == operario
            and fecha_inicio <= registro["FechaHora"] <= fecha_fin
        ):
            total += registro["Cantidad"]
    return total


def analisis_por_punto_origen(transporte_data, punto_origen, fecha_inicio, fecha_fin):
    """
    Calcular el total de carbon transportado desde origen en un rango

    Parámetros:
    - transporte_data(list): Lista que almacena los transporte.
    - punto_origen(str): Nombre del punto de origen
    - fecha_inicio(str): Fecha de inicio del analisis en formato 'YYYY-mm-dd'.
    - fecha_fin (str): Fecha del fin del analisis en formato 'YYYY-mm-dd'
    Retorna:
    - total(int): La cantidad total de carbon transportada del punto de origen segun las fechas de inicio y final.

    """
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    total = 0
    for registro in transporte_data:
        if (
            registro["PuntoOrigen"] == punto_origen
            and fecha_inicio <= registro["FechaHora"] <= fecha_fin
        ):
            total += registro["Cantidad"]
    return total


def generar_reporte(transporte_data):
    reporte = "Reporte de Transporte de Carbón:\n"
    for registro in transporte_data:
        reporte += f"{registro['FechaHora'].strftime('%Y-%m-%d %H:%M')}: {registro['Cantidad']} toneladas de {registro['PuntoOrigen']} por {registro['Operario']}\n"
    return reporte


# Ejemplo de uso
transporte_data = []
registrar_transporte(
    transporte_data, "Mina Norte", 500, "Juan Pérez", "2024-08-13 08:00"
)
registrar_transporte(transporte_data, "Mina Sur", 300, "Ana López", "2024-08-13 10:00")

print(analisis_por_operario(transporte_data, "Juan Pérez", "2024-08-01", "2024-08-13"))
print(
    analisis_por_punto_origen(transporte_data, "Mina Norte", "2024-08-01", "2024-08-13")
)

print(generar_reporte(transporte_data))

analisis_por_operario()
