# populate_db.py
import json
import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()
from productos.models import Product

# Ruta al archivo JSON
json_file_path = 'productos/data/productos.json'


def poblar_datos():
    # Cargar datos del archivo JSON
    with open(json_file_path, 'r') as file:
        productos_data = json.load(file)

    # Crear instancias del modelo y guardarlas en la base de datos
    for producto_data in productos_data[:5]:
        producto = Product(
            ProductId=producto_data['ProductId'],
            # Gender=producto_data['Gender'],
            Category=producto_data['Category'],
            # SubCategory=producto_data['SubCategory'],
            # ProductType=producto_data['ProductType'],
            # Colour=producto_data['Colour'],
            # Usage=producto_data['Usage'],
            ProductTitle=producto_data['ProductTitle'],
            ImageURL=producto_data['ImageURL'],
            # Image=producto_data['Image']
            Description=producto_data['SubCategory']
        )
        producto.save()

    print("Datos poblados exitosamente")


if __name__ == "__main__":
    poblar_datos()
