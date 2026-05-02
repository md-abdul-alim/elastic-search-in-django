from django.shortcuts import render
from django.http import JsonResponse
from elasticsearch_dsl.query import MultiMatch
from products.documents import ProductDocument

def search_product(request):
    query = request.GET.get('search', '')

    results = ProductDocument.search().query(
        "bool",
        should=[
            # {"match": {"title": query}}, # Fuzzy search, tolerates typos and variations
            {"match": {"title": {"query": query, "fuzziness": "AUTO"}}}, # Fuzzy search with automatic fuzziness: tolerates typos and variations. fuzziness: 1 allows for one edit (insertion, deletion, substitution), fuzziness: 2 allows for two edits, and so on. AUTO lets Elasticsearch determine the appropriate fuzziness based on the length of the search term.
            {"term": {"brand.name": query}} # Exact match, requires precise brand name
        ],
        minimum_should_match=1
    ).sort('_score', '-price').extra(size=30) # Sort by relevance score and then by price in descending order


    '''
    results = ProductDocument.search().query(
        MultiMatch(
            query=query,
            fields=['title^3', 'description', 'category', 'brand.name^2'], # Boost title and brand.name fields for higher relevance
            fuzziness='AUTO' # Enable fuzzy search to tolerate typos and variations
        )
    ).collapse(field='sku') # collapse ensure only one result per unique SKU, preventing duplicates in the search results. Which works like distinct in SQL
    '''

    results = results.execute()

    data = {
        'status': 'success',
        'message': 'Product search successful',
        'products': [
            {
                'id': hit.meta.id,
                'title': hit.title,
                'description': hit.description,
                'brand': hit.brand.to_dict() if hit.brand else None,
                'price': hit.price,
            }
            for hit in results
        ]
    }
    return JsonResponse(data)