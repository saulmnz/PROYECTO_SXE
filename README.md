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

**Website & eCommerce: Gestión de interfaz comercial y catálogo digital.**

**Inventario & Compras:Control de stock, reglas de abastecimiento y flujo de suministros.**


**Manufacturing (MRP):Motor de producción para el ensamblaje de equipos a medida. (PC BESTIAAA)**

**Facturación y Contabilidad: Registro contable de las operaciones, impuestos y tesorería.**

<img width="907" height="354" alt="image" src="https://github.com/user-attachments/assets/7a416bee-71e8-46aa-86df-f344edff3ff3" />



## 4. GESTIÓN DE PROYECTO 🟪
> **Se definieron los backlogs iniciales para priorizar las tareas de desarrollo y configuración :**

**Con la intención de tener una implementación ordenada y limpia de los requisitos funcionales, este módulo se ha estructurado siguiendo el patrón de diseño oficial de Odoo.**

<img width="1550" height="768" alt="image" src="https://github.com/user-attachments/assets/0343e6b8-4ee7-4164-99c8-b01f7b1126e6" />

<img width="1086" height="820" alt="image" src="https://github.com/user-attachments/assets/72f6feb6-96b1-482f-a3e6-d8f0b7df6d5d" />


## 5. INVENTARIO Y DATOS MAESTROS
> **Se definieron categorías para organizar el flujo de materiales y la valoración de inventario:**
* **Componentes: Materias primas para el proceso de ensamblaje.**
<img width="1136" height="162" alt="image" src="https://github.com/user-attachments/assets/c5b00a27-2851-40a8-8897-4f0b2765f7e2" />

* **PCs Ensamblados:Productos terminados destinados a la venta final.**
  
<img width="959" height="265" alt="CATEGORIA" src="https://github.com/user-attachments/assets/282a31b1-410f-40ef-ba64-1b798750a55c" />

> **Se crearon los siguientes requisitos a validar:**
* **Materias Primas: Procesador (CPU), Tarjeta Gráfica (GPU) y Torre.**
 
<img width="959" height="388" alt="PRODUCTO" src="https://github.com/user-attachments/assets/0f2614ee-9f76-495c-984d-31022c122e3a" />

<img width="959" height="332" alt="INFO MODULO VIGOTECH PRODUCTO" src="https://github.com/user-attachments/assets/783e5de6-7f29-48d9-8208-9e815e218af5" />


* **Producto Terminado:"PC Gaming Bestia", configurado con ruta de fabricación.**
<img width="1302" height="500" alt="image" src="https://github.com/user-attachments/assets/d1e7d16b-ca5c-4f53-af18-76d31cc25cf1" />


  

## 6. COMPROBACIÓN CICLO DE COMPRAS 🟪
> **Se ejecutó una compra completa para testear el desarrollo:**
**Registro de Proveedor:Alta de ficha de partner con condiciones de pago.**
<img width="959" height="364" alt="PROVEEDOR" src="https://github.com/user-attachments/assets/7c6df2d4-d70d-4002-bd90-673806e8002b" />

**Solicitud de Presupuesto (RFQ):Creación de pedido para componentes (CPU, GPU, Torre).**
**Recepción de Mercancía: Validación del albarán de entrada y cambios en el stock.**
 <img width="956" height="245" alt="STOCK DESPUES DE PEDIDO" src="https://github.com/user-attachments/assets/6764147e-3fde-48e6-bbb0-9266526ed03f" />
**Factura de Proveedor Generación, validación y registro del pago de la factura de compra, cerrando el ciclo de deuda con el proveedor.**
<img width="748" height="695" alt="image" src="https://github.com/user-attachments/assets/9fd7363c-0d88-4121-b90f-99cf8f168b1c" />

## 7. Ingeniería de Producto y Fabricación (MRP)
> **Se configuró la lógica de producción para automatizar el ensamblaje bajo demanda:**
* **Listas de Materiales (BoM):Definición de la estructura del producto "PC Gaming Bestia", con sus componentes (CPU, GPU, Torre) como necesarios.**
* **Orden de Producción:Ejecución de pruebas de fabricación donde el sistema descuenta automáticamente el stock de componentes y realiza el alta del producto terminado en el inventario.**
<img width="476" height="454" alt="ORDEN DE FABRICACION" src="https://github.com/user-attachments/assets/ec80064f-b69d-4162-a094-3fd12e51f7cf" />


## 8. FLUJO E ECOMMERCE 🟪
**Implementación del ciclo completo de venta desde el escaparate digital hasta el cobro:**
* **Publicación Web:Despliegue del producto en el *eCommerce* de Odoo, configurando estados de publicación y banners.**
  
<img width="470" height="242" alt="ORDENADOR PUBLICADO EN TIENDA" src="https://github.com/user-attachments/assets/8198c3f0-525e-40d3-b04b-bdaac63ab075" />

* **Gestión de Pedidos (SO):Trazabilidad completa desde la confirmación del pedido en la web hasta el backend administrativo.**

<img width="479" height="394" alt="COMPRO ORDENADOR" src="https://github.com/user-attachments/assets/9fde01e7-e619-4b92-ae9a-e16e32f505ff" />

<img width="477" height="316" alt="COMPRAR FINALIZAR ORDENADOR" src="https://github.com/user-attachments/assets/f37ec4fe-448c-4bd3-ab38-fa161f6bfe7d" />


<img width="474" height="329" alt="FINALIZAR COMPRA" src="https://github.com/user-attachments/assets/c111573b-093f-45a4-b4e5-2100479f08fe" />


<img width="479" height="270" alt="PEDIDO DE COMPRA" src="https://github.com/user-attachments/assets/daf589ec-5090-4c33-86b4-ab74f22c9376" />


<img width="474" height="393" alt="PEDIDO DEL ORDENADOR NO PAGADO" src="https://github.com/user-attachments/assets/6aa71754-938d-4ce0-8520-acfcd7036f58" />



* **Logística de Salida: Validación del Albarán de Entrega (*Delivery Order*), descontando el stock final del almacén.**

<img width="475" height="314" alt="ENTREGA PRODUCTO VALIDAD" src="https://github.com/user-attachments/assets/44d03594-1183-4308-92b3-2b550b2def49" />


## 9. GESTIÓN Y CIERRE CONTABLE 🟪
**Configuración de la capa contable para asegurar la integridad de los datos financieros:**
* **Datos Corporativos: Personalización de la compañía para la emisión de documentos.**
* **Facturación de Cliente: Emisión y validación de facturas desde los pedidos de venta.**
* **Conciliación de Pagos:Registro de los flujos de caja y cambio de estado a PAGADO mediante los diarios de banco/efectivo.**

## 10. INFORME 🟪
> **Se ha desarrollado un informe que mmuestre todas las características creadas en los productos de Vigotech**


**Mediante los campos creados anteriormenete se desarrolla un informe que contiene toda la información lista para mostrarle el producto al cliente. Se accede a este informe
propio mediante el icono del engranaje al lado del producto.**

<img width="769" height="319" alt="image" src="https://github.com/user-attachments/assets/3af363dc-e2ca-4ca3-b6ea-4f5d2899951f" />
<img width="455" height="627" alt="image" src="https://github.com/user-attachments/assets/9640ddba-cad0-4137-819b-0188be40e631" />



## 11. INTEGRACIÓN Y AUTOMATIZACIÓN EXTERNA (BONUSSS) 🟪
> **A mayores, se diseño un desarrollo que permite la conectividad mediante API externa de Odoo**
* **Script XML-RPC: Desarrollo de un script en **Python** que se conecta al ERP mediante protocolo XML-RPC.**
* **Funcionalidad:El script audita la base de datos remotamente para generar alertas de Stock Crítico, identificando productos por debajo del umbral de seguridad sin necesidad de acceder a la interfaz web.**

```Python

import xmlrpc.client

# CONEXIÓN
url = 'http://localhost:8069'
db = 'VIGO_TECH_1'
username = 'admin@example.com'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

# INTENTAMOS AUTENTICAR
try:
    uid = common.authenticate(db, username, password, {})
    if uid:
        print(f"CONECTAASTE: {uid}")
    else:
        print("ERROOOR, NO CONECTASTE.")
        exit()
except Exception as e:
    print(f"Error de conexión: {e}")
    exit()

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

#LA CONSULTA
print("BUSCANDO PRODUCTOS CON STOCK CRÍTICO (<10 ud)")

ids_productos = models.execute_kw(db, uid, password,
    'product.product', 'search',
    [[
        ['qty_available', '<', 10],
        ['qty_available', '>', -100]
    ]])

if ids_productos:
    # LEEMOS NOMBRES Y CANTIDADES
    productos = models.execute_kw(db, uid, password,
        'product.product', 'read',
        [ids_productos],
        {'fields': ['name', 'qty_available', 'standard_price']})

    for prod in productos:
        nombre = prod['name']
        stock = prod['qty_available']
        coste = prod['standard_price']
        print(f"ALERTA: {nombre} | STOCK: {stock} | COSTE: {coste}€")
else:
    print("TODO BIEN, NO HAY PRODUCTOS EN STOCK CRÍTICO.")



```

---
