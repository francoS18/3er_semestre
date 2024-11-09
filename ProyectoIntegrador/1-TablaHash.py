from TAD import TablaHash

# Creación de la tabla hash para la base de datos de empleados
base_de_datos_empleados = TablaHash(15)

# Agregar empleados a la base de datos
base_de_datos_empleados.agregar(1)  # Empleado con número de identificación 1001
base_de_datos_empleados.agregar(2)  # Empleado con número de identificación 1002
base_de_datos_empleados.agregar(3)  # Empleado con número de identificación 1003
base_de_datos_empleados.agregar(4)  # Empleado con número de identificación 1004
base_de_datos_empleados.agregar(5)  # Empleado con número de identificación 1005
base_de_datos_empleados.agregar(6)  # Empleado con número de identificación 1006
base_de_datos_empleados.agregar(7)  # Empleado con número de identificación 1007
base_de_datos_empleados.agregar(8)  # Empleado con número de identificación 1008
base_de_datos_empleados.agregar(9)  # Empleado con número de identificación 1009
base_de_datos_empleados.agregar(10)  # Empleado con número de identificación 1010
base_de_datos_empleados.agregar(11)  # Empleado con número de identificación 1011
base_de_datos_empleados.agregar(12)  # Empleado con número de identificación 1012
base_de_datos_empleados.agregar(13)  # Empleado con número de identificación 1013
base_de_datos_empleados.agregar(14)  # Empleado con número de identificación 1014
base_de_datos_empleados.agregar(15)  # Empleado con número de identificación 1015

# Manejar colisiones
colisiones = []
for i in range(1, 16):
    if base_de_datos_empleados.buscar(i) is None:
        base_de_datos_empleados.agregar(i)
    else:
        colisiones.append(i)

# Mostrar contenido de la tabla hash (solo para fines ilustrativos)
print("Contenido de la tabla hash:")
for i, bucket in enumerate(base_de_datos_empleados.tabla):
    if bucket is not None:
        print(f"Índice {i}: Empleado con ID {bucket}")

# Mostrar colisiones
print("\nColisiones:")
print(colisiones)