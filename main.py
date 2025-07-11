from db import crear_base_datos, crear_tabla_categorias, crear_tabla_producto
import os # Para limpiar la terminal y cree una experiencia al usuario más agradable
import time # Para crear transiciones mas sutiles de menus
from menu import mostrar_menu

def iniciar_sistema():
    # ARRANQUE DE SISTEMA Y SALUDO INICIAL
    print("╔═════════════════════════════════════════════════════╗")
    print("║  🎉 ¡BIENVENIDO AL PROYECTO INTEGRADOR FINAL! 🎉   ║")
    print("╚═════════════════════════════════════════════════════╝")
    time.sleep(0.5)
    crear_base_datos("inventario.db")
    crear_tabla_categorias()
    crear_tabla_producto()
    mostrar_menu()
    os.system('cls')
    time.sleep(0.5)

if __name__ == "__main__":
    iniciar_sistema()
