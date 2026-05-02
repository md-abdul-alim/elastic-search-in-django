from django.shortcuts import render
from django.http import JsonResponse
from products.documents import ProductDocument

def search_product(request):
    products = []

    query = request.GET.get('search', '')
    results = ProductDocument.search().query(
        "match",
        title=query,
    )

    results = results.execute()

    for hit in results:
        products.append({
            'id': hit.meta.id,
            'title': hit.title,
            'description': hit.description,
            'brand': hit.brand.to_dict() if hit.brand else None,
            'price': hit.price,
        })

    data = {
        'status': 'success',
        'message': 'Product search successful',
        'products': products
    }
    return JsonResponse(data)