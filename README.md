📌 Proyecto Integrador CURSO INICIAL PYTHON Comisión 25009 

🔹 Descripción
Este proyecto consiste en el desarrollo de una aplicación en Python para gestionar información de clientes, productos y pedidos mediante un sistema CRUD básico por Terminal.
La aplicación permite:
- Registrar nuevos usuarios y productos.
- Consultar datos existentes con filtros y ordenamiento.
- Modificar información de usuarios, productos y pedidos.
- Eliminar registros de la base de datos temporal.
- Gestionar pedidos, incluyendo cambios de estado y cancelaciones.

🔹 Requisitos
Para ejecutar el proyecto, asegúrate de tener instalado:
- Python 3.10 o superior
- Bibliotecas requeridas (datetime, re, os, time)

🔹 Instalación
- Clonar el repositorio:
git clone https://github.com/tu_usuario/proyecto-integrador.git
cd proyecto-integrador
- Ejecutar el archivo principal:
python main.py



🔹 Uso
Menú Login
Al iniciar el programa, verás el siguiente menú:
- 📝 Registrarse
- 🔒 Iniciar sesión

Menú Principal
- 📝 Gestionar mis Datos
- 📦 Gestión de Productos
- 🛒 Gestión de Pedidos

Cada módulo contiene submenús para realizar operaciones CRUD.

Ejemplo de registro de producto
productos.append({
    "codigo": 107,
    "nombre": "Teclado Mecánico",
    "precio": 120,
    "descripcion": "Teclado RGB con switches azules",
    "categoria": "Tecnología"
})

🔹 Mejoras a Futuro
✔️ Control de permisos por usuario
✔️ Validación de productos duplicados
✔️ Implementación de funciones para modularizar
✔️ Persistencia con SQLite
✔️ Reporte de historial de pedidos

🔹 Contribución
Si deseas contribuir al proyecto:
- Haz un fork del repositorio.
- Crea una nueva rama (git checkout -b mejora-nueva).
- Haz tus cambios y envía un pull request.

🔹 Licencia
Este proyecto se distribuye bajo la licencia ClaudioCGG
