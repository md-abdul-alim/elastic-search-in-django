from django.shortcuts import render
from django.http import JsonResponse


def search_product(request):

    data = {
        'status': 'success',
        'message': 'Product search successful',
        'products': [
            {
                'id': 1,
                'name': 'Product 1',
                'price': 10.99
            },
            {
                'id': 2,
                'name': 'Product 2',
                'price': 19.99
            }
        ]
    }
    return JsonResponse(data)