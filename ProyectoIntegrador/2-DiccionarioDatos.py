from TAD import Diccionario

# Base de datos de usuarios
bd_usuarios = Diccionario()

# Agregar usuarios
bd_usuarios.agregar("usuario1", {"nombre": "Pedro", "correo": "pedro@example.com", "edad": 30})
bd_usuarios.agregar("usuario2", {"nombre": "Juan", "correo": "juan@example.com", "edad": 25})
bd_usuarios.agregar("usuario3", {"nombre": "Diego", "correo": "diego@example.com", "edad": 35})

# Ver datos
print(bd_usuarios.verDato("usuario1"))

# Eliminación de datos
bd_usuarios.remover("usuario3")
print(bd_usuarios.diccionario)