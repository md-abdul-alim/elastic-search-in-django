# Update Eleasticsearch index for a product data manually.

from products.models import Product, Brand
from products.documents import ProductDocument

product = Product.objects.get(id=1)
product.title = "Updated Product Title"
product.save()

ProductDocument().update(product)

products = Product.objects.all()
for product in products:
    brand , _ = Brand.objects.get_or_create(brand_name=product.brand)
    product.update(brand_name=brand)

# ProductDocument().delete(id=420)