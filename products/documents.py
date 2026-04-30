from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Product

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = "products"
        # See Elasticsearch Indices API reference for available settings
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    
    brand = fields.ObjectField(properties={
        'name': fields.KeywordField(),
        'description': fields.TextField(),
    })

    class Django:
        model = Product
        fields = [
            "title",
            "description",
            "category",
            "price",
            "sku",
            "thumbnail",
        ]