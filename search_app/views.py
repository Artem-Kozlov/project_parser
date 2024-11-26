from django.shortcuts import render
from search_app.ozon_parser import get_products_links

def search_view(request):
    links = []
    query = request.GET.get('query')
    if query:
        links = get_products_links(item_name=query)

    return render(request, 'search_app/search.html', {'query': query, 'links': links})
