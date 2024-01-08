import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('catalog_data.json') as f:
            catalog_data = json.load(f)

        product_list = [Product(**product_item['fields']) for product_item in catalog_data
                        if product_item.get('model') == 'catalog.product']

        category_list = [Category(**category_item['fields']) for category_item in catalog_data
                         if category_item.get('model') == 'catalog.category']

        Product.objects.all().delete()
        Product.objects.bulk_create(product_list)

        Category.objects.all().delete()
        Category.objects.bulk_create(category_list)
