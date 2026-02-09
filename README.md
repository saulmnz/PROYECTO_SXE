# PROYECTO SXE 💜💜

***AUTORES: Saúl Álvarez, Adrián Miguez, Sofía Otero***

***MÓDULO: SISTEMAS DE XESTIÓN EMPRESARIAL***

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d7a82761-ad58-4c8e-baff-d130a5c27594" />

---

## 1. INTRODUCCIÓN Y OBJETIVO 🟪

>[!NOTE]
>***El objetivo de este proyecto ha sido la transformación digital de la empresa "Vigo-Tech Solutions", migrando su modelo de negocio físico a una arquitectura online mediante la implantación del ERP Odoo. El proyecto abarca desde la configuración de infraestructura hasta la automatización de procesos de negocio complejos (MRP, eCommerce y Contabilidad).***

## 2. CONFIGURACIÓN DE INFRAESTRUCTURA 🟪

>**El proyecto inició con el establecimiento de un entorno de desarrollo robusto y escalable:**

- **Contenerización: Despliegue de la arquitectura mediante Docker Compose.**

```yaml
services:
  db:
    image: postgres:17
    container_name: vigo_tech_db
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  web:
    image: odoo:18.0
    container_name: vigo_tech_app
    depends_on:
      - db
    ports:
      - "8069:8069"
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo
      - ODOO_MASTER_PASSWD=odoo
      - ADDONS_PATH=/mnt/extra-addons,/etc/odoo/addons
    volumes:
      - web_data:/var/lib/odoo
      - ./addons:/mnt/extra-addons
    restart: unless-stopped

  pgadmin:
    image: dpage/pgadmin4
    container_name: vigo_tech_pgadmin
    depends_on:
      - db
    ports:
      - "5050:80"
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@example.com
      - PGADMIN_DEFAULT_PASSWORD=admin
    volumes:
      - pgadmin_data:/var/lib/pgadmin
    restart: unless-stopped
volumes:
  postgres_data:
  web_data:
  pgadmin_data:
```

- **Módulo: Creación de un módulo personalizado de Odoo (`scaffold`) para alojar las personalizaciones y datos maestros.**
- **Herencia de Modelos: Se aplicó herencia técnica sobre el modelo `product.template` para extender las funcionalidades nativas del catálogo de productos y adaptarlas al sector hardware de la empresa.**

```Python
from odoo import models, fields

class Producto(models.Model):
    # AQUÍ LE HEREDO EL MODELO DE LOS PRODUCTOS
    _inherit = 'product.template' 

    # CAMPO DE SELECCIÓN DE COMPONENTES
    vigotech_component_type = fields.Selection([
        ('cpu', 'Procesador (CPU)'),
        ('gpu', 'Tarjeta Gráfica (GPU)'),
        ('ram', 'Memoria RAM'),
        ('motherboard', 'Placa Base'),
        ('storage', 'Almacenamiento (SSD/HDD)'),
        ('case', 'Torre/Caja'),
        ('psu', 'Fuente de Alimentación'),
        ('peripheral', 'Periférico'),
        ('other', 'Otros')
    ], string='Tipo de Componente (Vigo-Tech)', help='Categoría técnica para ensamblaje')

    # CAMPO PARA GARANTÍASSS
    vigotech_warranty_months = fields.Integer(
        string='Garantía (Meses)', 
        default=36,
        help='Meses de garantía ofrecidos por el fabricante'
    )
    
    vigotech_tech_specs = fields.Text(
        string='Especificaciones Técnicas Detalladas'
    )
```



## 3. ECOSISTEMA DE MÓDULOS 🟪

> **Se realizó la instalación y orquestación de la suite de aplicaciones necesaria para el flujo empresarial:**

- **Website & eCommerce: Gestión de interfaz comercial y catálogo digital.**
- **Inventario & Compras: Control de stock, reglas de abastecimiento y flujo de suministros.**
- **Manufacturing (MRP): Motor de producción para el ensamblaje de equipos a medida. (PC BESTIAAA)**
- **Facturación y Contabilidad: Registro contable de las operaciones, impuestos y tesorería.**



## 4. GESTIÓN DE PROYECTO 🟪
> **Se definieron los backlogs iniciales para priorizar las tareas de desarrollo y configuración :**

**Con la intención de tener una implementación ordenada y limpia de los reqiuisitos funcionales**

## 5. INVENTARIO Y DATOS MAESTROS
### Estructura de Categorías
> **Se definieron categorías para organizar el flujo de materiales y la valoración de inventario:**
* **Componentes:** Materias primas para el proceso de ensamblaje.
* **PCs Ensamblados:** Productos terminados destinados a la venta final.
  
<img width="959" height="265" alt="CATEGORIA" src="https://github.com/user-attachments/assets/282a31b1-410f-40ef-ba64-1b798750a55c" />

### Catálogo y Variantes
> **Se crearon los siguientes requisitos a validar:**
* **Materias Primas:** Procesador (CPU), Tarjeta Gráfica (GPU) y Torre.
 
<img width="959" height="388" alt="PRODUCTO" src="https://github.com/user-attachments/assets/0f2614ee-9f76-495c-984d-31022c122e3a" />

<img width="959" height="332" alt="INFO MODULO VIGOTECH PRODUCTO" src="https://github.com/user-attachments/assets/783e5de6-7f29-48d9-8208-9e815e218af5" />


* **Producto Terminado:** "PC Gaming Bestia", configurado con ruta de fabricación.
* 
* **Gestión de Variantes:** Implementación de atributos (ej: *Color: Negro/Blanco*) .


## 6. COMPROBACIÓN CICLO DE COMPRAS 🟪
> **Se ejecutó una compra completa para testear el desarrollo:**
1. **Registro de Proveedor:** Alta de ficha de partner con condiciones de pago.
2. **Solicitud de Presupuesto (RFQ):** Creación de pedido para componentes (CPU, GPU, Torre).
3. **Recepción de Mercancía:** Validación del albarán de entrada y cambios en el stock.
4. **Factura de Proveedor:** Generación, validación y **registro del pago** de la factura de compra, cerrando el ciclo de deuda con el proveedor.

## 7. Ingeniería de Producto y Fabricación (MRP)
Se configuró la lógica de producción para automatizar el ensamblaje bajo demanda:
* **Listas de Materiales (BoM):** Definición de la estructura del producto "PC Gaming Bestia", con sus componentes (CPU, GPU, Torre) como necesarios.
* **Orden de Producción:** Ejecución de pruebas de fabricación donde el sistema descuenta automáticamente el stock de componentes y realiza el alta del producto terminado en el inventario.

## 8. FLUJO E ECOMMERCE 🟪
Implementación del ciclo completo de venta desde el escaparate digital hasta el cobro:
* **Publicación Web:** Despliegue del producto en el *eCommerce* de Odoo, configurando estados de publicación y banners.
* 
<img width="470" height="242" alt="ORDENADOR PUBLICADO EN TIENDA" src="https://github.com/user-attachments/assets/8198c3f0-525e-40d3-b04b-bdaac63ab075" />

* **Gestión de Pedidos (SO):** Trazabilidad completa desde la confirmación del pedido en la web hasta el backend administrativo.

<img width="479" height="394" alt="COMPRO ORDENADOR" src="https://github.com/user-attachments/assets/9fde01e7-e619-4b92-ae9a-e16e32f505ff" />

<img width="477" height="316" alt="COMPRAR FINALIZAR ORDENADOR" src="https://github.com/user-attachments/assets/f37ec4fe-448c-4bd3-ab38-fa161f6bfe7d" />


<img width="474" height="329" alt="FINALIZAR COMPRA" src="https://github.com/user-attachments/assets/c111573b-093f-45a4-b4e5-2100479f08fe" />


<img width="479" height="270" alt="PEDIDO DE COMPRA" src="https://github.com/user-attachments/assets/daf589ec-5090-4c33-86b4-ab74f22c9376" />


<img width="474" height="393" alt="PEDIDO DEL ORDENADOR NO PAGADO" src="https://github.com/user-attachments/assets/6aa71754-938d-4ce0-8520-acfcd7036f58" />



* **Logística de Salida:** Validación del Albarán de Entrega (*Delivery Order*), descontando el stock final del almacén.

<img width="475" height="314" alt="ENTREGA PRODUCTO VALIDAD" src="https://github.com/user-attachments/assets/44d03594-1183-4308-92b3-2b550b2def49" />


## 9. Gestión Financiera y Cierre Contable
Configuración de la capa contable para asegurar la integridad de los datos financieros:
* **Datos Corporativos:** Personalización de la compañía (Logo, Dirección fiscal en Vigo) para la emisión formal de documentos.
* **Facturación de Cliente:** Emisión y validación de facturas desde los pedidos de venta.
* **Conciliación de Pagos:** Registro de los flujos de caja y cambio de estado a **"PAGADO"** (Ribbon verde) mediante los diarios de banco/efectivo, resolviendo conflictos de cuentas de ingresos predeterminadas.

## 10. INTEGRACIÓN Y AUTOMATIZACIÓN EXTERNA (BONUSSS)
> **A mayores, se diseño un desarrollo que permite la conectividad mediante API externa de Odoo**
* **Script XML-RPC:** Desarrollo de un script en **Python** que se conecta al ERP mediante protocolo XML-RPC.
* **Funcionalidad:** El script audita la base de datos remotamente para generar alertas de **"Stock Crítico"**, identificando productos por debajo del umbral de seguridad sin necesidad de acceder a la interfaz web.

---
