from calendar import c
import requests


# ici l'adresse que nous allons appeler
endpoint = "http://localhost:8000/api/v1"

# Données

data = {
    "name": "Product 1",
    "description": "Description 1",
    "price": 10.0,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
}

# On retrouve plusieurs verbe utilisé lors d'appel http
# - GET : Récupérer des données
# - POST : Envoyer des données
# - PUT : Mettre à jour des données
# - PATCH : Mettre à jour partiellement des données
# - DELETE : Supprimer des données

# ici la methode appelé qui sera post
response = requests.post(endpoint + "/products", data=data)

# affichage de la réponse
print("response Product : ", response.json())
print("response.status_code Product : ", response.status_code)