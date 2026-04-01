from django.core.management.base import BaseCommand
from inventory.models import Category, Product, Supplier, Sale
from django.contrib.auth.models import User
from decimal import Decimal
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Populate the database with sample data for testing'

    def handle(self, *args, **options):
        # Create sample categories
        categories = [
            {'name': 'Laptops', 'description': 'Portable computers'},
            {'name': 'Desktops', 'description': 'Desktop computers'},
            {'name': 'Monitors', 'description': 'Computer displays'},
            {'name': 'Printers', 'description': 'Printing devices'},
            {'name': 'Networking', 'description': 'Network equipment'},
        ]

        for cat_data in categories:
            Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )

        # Create sample suppliers
        suppliers = [
            {'name': 'TechCorp Ltd', 'email': 'info@techcorp.com', 'phone': '+254700000001'},
            {'name': 'Global Electronics', 'email': 'sales@globalelec.com', 'phone': '+254700000002'},
            {'name': 'Kenya Tech Solutions', 'email': 'contact@kts.co.ke', 'phone': '+254700000003'},
        ]

        for sup_data in suppliers:
            Supplier.objects.get_or_create(
                name=sup_data['name'],
                defaults={
                    'email': sup_data['email'],
                    'phone': sup_data['phone']
                }
            )

        # Get created objects
        categories = Category.objects.all()
        suppliers = Supplier.objects.all()

        # Create sample products
        products_data = [
            {'name': 'Dell Latitude 5420', 'description': 'Business laptop', 'price': Decimal('85000.00'), 'stock_quantity': 15, 'category': categories[0], 'supplier': suppliers[0]},
            {'name': 'HP Pavilion Desktop', 'description': 'Home desktop PC', 'price': Decimal('65000.00'), 'stock_quantity': 8, 'category': categories[1], 'supplier': suppliers[1]},
            {'name': 'Samsung 27" Monitor', 'description': '4K UHD Monitor', 'price': Decimal('35000.00'), 'stock_quantity': 12, 'category': categories[2], 'supplier': suppliers[0]},
            {'name': 'Canon PIXMA Printer', 'description': 'All-in-one inkjet printer', 'price': Decimal('25000.00'), 'stock_quantity': 6, 'category': categories[3], 'supplier': suppliers[2]},
            {'name': 'TP-Link Router', 'description': 'Wireless N router', 'price': Decimal('8000.00'), 'stock_quantity': 20, 'category': categories[4], 'supplier': suppliers[1]},
            {'name': 'Lenovo ThinkPad', 'description': 'Professional laptop', 'price': Decimal('95000.00'), 'stock_quantity': 10, 'category': categories[0], 'supplier': suppliers[2]},
        ]

        for prod_data in products_data:
            Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    'description': prod_data['description'],
                    'price': prod_data['price'],
                    'stock_quantity': prod_data['stock_quantity'],
                    'category': prod_data['category'],
                    'supplier': prod_data['supplier']
                }
            )

        # Create sample sales
        products = Product.objects.all()
        today = date.today()

        for i in range(20):
            product = random.choice(products)
            quantity = random.randint(1, 3)
            sale_date = today - timedelta(days=random.randint(0, 30))

            # Ensure we don't sell more than available stock
            if product.stock_quantity >= quantity:
                Sale.objects.get_or_create(
                    product=product,
                    quantity=quantity,
                    sale_date=sale_date,
                    defaults={
                        'unit_price': product.price,
                        'total_price': product.price * quantity
                    }
                )
                # Update stock
                product.stock_quantity -= quantity
                product.save()

        # Create a test user if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data')
        )