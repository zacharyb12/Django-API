from django.http import JsonResponse

def home(request):
    headers = request.headers
    post_data = request.POST
    params = request.GET
    print("---------------------------------------------------")
    print("Headers:", headers)
    print("---------------------------------------------------")
    print("GET Data:", params)
    print("---------------------------------------------------")
    print("POST Data:", post_data)
    print("---------------------------------------------------")
    print()
    
    return JsonResponse({"users": [
        {"id": 1, "name": "John Doe", "email": "john@example.com" },
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
    ]
                         })

def products(request):
    headers = request.headers
    post_data = request.POST
    params = request.GET

    print("---------------------------------------------------")
    print("Headers:", headers)
    print("---------------------------------------------------")
    print("GET Data:", params)
    print("---------------------------------------------------")
    print("POST Data:", post_data)
    print("---------------------------------------------------")
    print()

    return JsonResponse({"products": [
        {"id": 1, "name": "Product 1", "description": "Description 1", "price": 10.0},
        {"id": 2, "name": "Product 2", "description": "Description 2", "price": 20.0},
    ]
    })