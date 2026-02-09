# 🚀 PROYECTO SXE: Implantación ERP para "Vigo-Tech Solutions"

**Autores:** [Vuestros Nombres]  
**Curso:** Desarrollo de Aplicaciones Multiplataforma (DAM)  
**Módulo:** Sistemas de Gestión Empresarial  

---

## 1. Introducción y Objetivo
El objetivo de este proyecto ha sido la transformación digital de la empresa **"Vigo-Tech Solutions"**, migrando su modelo de negocio físico a una arquitectura 100% Online mediante la implantación del ERP Odoo. El proyecto abarca desde la configuración de infraestructura hasta la automatización de procesos de negocio complejos (MRP, eCommerce y Contabilidad).

## 2. Configuración de Infraestructura y Arquitectura
El proyecto inició con el establecimiento de un entorno de desarrollo robusto y escalable:
* **Contenerización:** Despliegue de la arquitectura mediante **Docker** y **Docker Compose** para asegurar la paridad entre entornos de desarrollo y producción.
* **Bootstrapping del Módulo:** Creación de un módulo personalizado de Odoo (`scaffold`) para alojar las personalizaciones y datos maestros.
* **Herencia de Modelos:** Se aplicó herencia técnica sobre el modelo `product.template` para extender las funcionalidades nativas del catálogo de productos y adaptarlas al sector hardware.

## 3. Ecosistema de Módulos
Se realizó la instalación y orquestación de la suite de aplicaciones necesaria para el flujo empresarial:
* **Website & eCommerce:** Gestión de interfaz comercial (Front-end) y catálogo digital.
* **Inventario & Compras:** Control de stock, reglas de abastecimiento y flujo de suministros.
* **Manufacturing (MRP):** Motor de producción para el ensamblaje de equipos a medida.
* **Facturación y Contabilidad:** Registro contable de las operaciones, impuestos y tesorería.

## 4. Gestión del Proyecto (Backlog)
Se definieron los backlogs iniciales para priorizar las tareas de desarrollo y configuración, asegurando una implementación organizada de los requisitos funcionales (Sprints de configuración).

## 5. Configuración de Inventario y Datos Maestros
### Estructura de Categorías
Se definieron categorías estratégicas para organizar el flujo de materiales y la valoración de inventario:
* **Componentes:** Materias primas (*Raw Materials*) para el proceso de ensamblaje.
* **PCs Ensamblados:** Productos terminados destinados a la venta final.

### Catálogo y Variantes
Para validar el sistema, se dieron de alta registros complejos:
* **Materias Primas:** Procesador (CPU), Tarjeta Gráfica (GPU) y Torre.
* **Producto Terminado:** "PC Gaming Bestia", configurado con ruta de fabricación.
* **Gestión de Variantes:** Implementación de atributos (ej: *Color: Negro/Blanco*) para demostrar la capacidad del ERP de gestionar múltiples SKUs bajo una misma plantilla de producto.

## 6. Validación del Flujo de Suministros (Compras)
Se ejecutó un ciclo completo de aprovisionamiento (*Procure-to-Pay*) para testear la integración:
1. **Registro de Proveedor:** Alta de ficha de partner con condiciones de pago.
2. **Solicitud de Presupuesto (RFQ):** Creación de pedido para componentes (CPU, GPU, Torre).
3. **Recepción de Mercancía:** Validación del albarán de entrada (*Warehouse In*) aumentando el stock disponible.
4. **Factura de Proveedor:** Generación, validación y **registro del pago** de la factura de compra, cerrando el ciclo de deuda con el proveedor.

## 7. Ingeniería de Producto y Fabricación (MRP)
Se configuró la lógica de producción para automatizar el ensamblaje bajo demanda:
* **Listas de Materiales (BoM):** Definición de la estructura del producto "PC Gaming Bestia", vinculando los componentes (CPU, GPU, Torre) como insumos necesarios.
* **Orden de Producción:** Ejecución de pruebas de fabricación donde el sistema descuenta automáticamente el stock de componentes y realiza el alta del producto terminado en el inventario.

## 8. Flujo Comercial y E-commerce (Order-to-Cash)
Implementación del ciclo completo de venta desde el escaparate digital hasta el cobro:
* **Publicación Web:** Despliegue del producto en el *eCommerce* de Odoo, configurando estados de publicación y banners promocionales ("Ribbons").
* **Gestión de Pedidos (SO):** Trazabilidad completa desde la confirmación del pedido en la web hasta el backend administrativo.
* **Logística de Salida:** Validación del Albarán de Entrega (*Delivery Order*), descontando el stock final del almacén.

## 9. Gestión Financiera y Cierre Contable
Configuración de la capa contable para asegurar la integridad de los datos financieros:
* **Datos Corporativos:** Personalización de la compañía (Logo, Dirección fiscal en Vigo) para la emisión formal de documentos.
* **Facturación de Cliente:** Emisión y validación de facturas desde los pedidos de venta.
* **Conciliación de Pagos:** Registro de los flujos de caja y cambio de estado a **"PAGADO"** (Ribbon verde) mediante los diarios de banco/efectivo, resolviendo conflictos de cuentas de ingresos predeterminadas.

## 10. Integración y Automatización Externa (Bonus Técnico)
Como valor añadido al proyecto, se desarrolló una solución de conectividad mediante la API externa de Odoo:
* **Script XML-RPC:** Desarrollo de un script en **Python** que se conecta al ERP mediante protocolo XML-RPC.
* **Funcionalidad:** El script audita la base de datos remotamente para generar alertas de **"Stock Crítico"**, identificando productos por debajo del umbral de seguridad sin necesidad de acceder a la interfaz web.

---
