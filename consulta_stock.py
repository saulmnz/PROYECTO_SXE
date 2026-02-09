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


