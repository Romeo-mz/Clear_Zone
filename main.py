import folium
import requests
import os

if os.path.isfile('map.html'):
    os.remove('map.html')

# Coordonnées GPS du centre de la zone à rechercher
center = (44.666865, 3.010133)

# Rayon de la zone à rechercher, en kilomètres
search_radius = 50

# Rayon autour de chaque point de la zone à vérifier la présence de bâtiments, en kilomètres
building_radius = 5

# Nombre maximal de bâtiments autorisé dans le rayon de building_radius autour d'un point
max_buildings = 100

# Calcule la limite supérieure et inférieure de la zone à rechercher
lat_range = (center[0] - 0.001 * search_radius, center[0] + 0.001 * search_radius)

lon_range = (center[1] - 0.017 * search_radius, center[1] + 0.017 * search_radius)


# Initialise la carte
map = folium.Map(location=center, zoom_start=10)

# Boucle sur chaque point dans la zone à rechercher
for lat in range (int(lat_range[0] * 10 ), int(lat_range[1] * 10)):
    for lon in range(int(lon_range[0] * 10), int(lon_range[1] * 10)):
        point = (lat/10, lon/10)

        # Requête l'API OpenStreetMap pour récupérer les informations sur les bâtiments autour du point
        url = f"https://overpass-api.de/api/interpreter?data=[out:json];way(around:{building_radius * 1000},{point[0]},{point[1]})[building];out;"
        response = requests.get(url)
        print(response.content)

        if response.content and response.json():
            data = response.json()

        else:
            print(f"No data found for point {point}")
            continue

        # Vérifie s'il y a moins de max_buildings bâtiments autour du point
        if len(data["elements"]) <= max_buildings:
            # Ajoute le point à la carte
            folium.Marker(location=point).add_to(map)

# Affiche la carte
map.save('map.html')
