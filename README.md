# PROYECTO SXE 👨‍💻
## 1. Configuración de Infraestructura y Arquitectura
El proyecto inició con el establecimiento de un entorno de desarrollo robusto y escalable:

*   **Contenedores:** Despliegue de la arquitectura mediante Docker para asegurar la paridad entre entornos.
*   **Bootstrapping del Módulo:** Creación de un módulo personalizado de Odoo.
*   **Herencia de Modelos:** Se aplicó herencia técnica sobre el modelo `product.template` para extender las funcionalidades nativas del catálogo de productos.

## 2. Ecosistema de Módulos
Se realizó la instalación y configuración de la suite base necesaria para el flujo empresarial:

*   **Ventas & Website:** Gestión de interfaz comercial y catálogo digital.
*   **Inventario & Compras:** Control de existencias y flujo de suministros.
*   **Manufacturing (MRP):** Motor de producción para el ensamblaje.
*   **Facturación:** Registro contable de las operaciones.

## 3. Gestión del Proyecto (Backlog)
Se definieron los backlogs iniciales para priorizar las tareas de desarrollo y configuración, asegurando una implementación organizada de los requisitos funcionales.

## 4. Configuración de Inventario y Datos Maestros

### Estructura de Categorías
Se definieron dos categorías principales para organizar el flujo de materiales:

*   **Componentes:** Materias primas para el proceso de ensamblaje.
*   **PCs Ensamblados:** Productos terminados destinados a la venta.

### Catálogo de Productos (Datos de Prueba)
Para validar el sistema, se dieron de alta los siguientes registros:

*   **Materias Primas:** Procesador, Tarjeta Gráfica y Torre (Caja).
*   **Producto Terminado:** Se creó el producto "PC Gaming Bestia", configurado con la ruta de **Fabricación (Manufacture)**.

## 5. Validación del Flujo de Suministros
Se ejecutó un ciclo completo de aprovisionamiento para testear la integración:

1.  **Registro de Proveedor:** Creación de ficha de proveedor con datos de prueba.
2.  **Orden de Compra (PO):** Selección de los componentes creados (procesador, gráfica y torre).
3.  **Confirmación:** Validación del pedido de compra para la entrada de stock en el almacén.
