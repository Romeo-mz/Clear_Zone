# Clear Zone

Ce projet a pour but de trouver une zone "claire" à partir d'un point central donné. Une zone est considérée comme "claire" si elle ne contient pas plus de 100 bâtiments dans un rayon de 5 km autour de chaque point. 

## Utilisation

- Assurez-vous d'avoir Python 3.x installé sur votre ordinateur.
- Cloner le projet en exécutant `git clone https://github.com/Romeo-mz/Clear_Zone.git` dans votre terminal.
- Dans le terminal, naviguez vers le répertoire contenant le code et exécutez `pip install -r requirements.txt` pour installer les dépendances nécessaires.
- Exécutez `python main.py` pour lancer le programme.

## Paramètres

Le programme contient les paramètres suivants:

- `center`: les coordonnées GPS du point central de la zone à rechercher.
- `search_radius`: le rayon de la zone à rechercher, en kilomètres.
- `building_radius`: le rayon autour de chaque point de la zone à vérifier la présence de bâtiments, en kilomètres.
- `max_buildings`: le nombre maximal de bâtiments autorisé dans le rayon de `building_radius` autour d'un point.
