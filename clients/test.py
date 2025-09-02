# ici nous allons pouvoir simuler un front-end en demandant un appel http
import requests


# ici l'adresse que nous allons appeler
endpoint = "http://localhost:8000/api/v1"

# On retrouve plusieurs verbe utilisé lors d'appel http
# - GET : Récupérer des données
# - POST : Envoyer des données
# - PUT : Mettre à jour des données
# - PATCH : Mettre à jour partiellement des données
# - DELETE : Supprimer des données

# ici la methode appelé qui sera get 
response = requests.get(endpoint)

# affichage de la réponse
print("response : ", response.json())
print("response.status_code : ", response.status_code)


responseFilter = requests.get(endpoint + "/?filter=chaussures")

# affichage de la réponse
print("responseFilter : ", responseFilter.json())
print("responseFilter.status_code : ", responseFilter.status_code)
