from db import (
    crear_base_datos,
    crear_tabla_categorias,
    crear_tabla_producto,
    crear_tabla_stock  # Asegurate de tener esta función en db.py
)
import os
import time
from menu import mostrar_menu

def iniciar_sistema():
    print("╔═════════════════════════════════════════════════════╗")
    print("║  🎉 ¡BIENVENIDO AL PROYECTO INTEGRADOR FINAL! 🎉   ║")
    print("╚═════════════════════════════════════════════════════╝")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    crear_base_datos("inventario.db")
    crear_tabla_categorias()
    crear_tabla_producto()
    crear_tabla_stock()

    time.sleep(0.5)

    mostrar_menu()

if __name__ == "__main__":
    iniciar_sistema()
