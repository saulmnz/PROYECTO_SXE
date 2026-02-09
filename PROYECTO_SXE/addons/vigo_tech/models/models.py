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