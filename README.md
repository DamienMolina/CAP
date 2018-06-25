# Scripts
## Introduction
Ici, je recenserai des scripts en rapport avec la course à pied, et toutes les données autour (vitesse, distance, résultats, etc...)
Aujourd'hui, deux types d'analyse de résultats:
* Un ekiden c'est à dire un marathon couru en relais. Les distances classiques sont 5/10/5/10/5/7.195km.
* Une course dans un format particulier, 2 partenaires pour 3 boucles dans un village:
  * La première boucle par le premier coureur,
  * la deuxième boucle par le deuxième coureur,
  * la troisième boucle par les deux coureurs.

## Ekiden
Le fichier *csv_reader.py* lit le fichier *constantes.py* composé de:
* **csv_ekiden**, position du fichier d'entrée
* **dossier_sortie**
* La liste des champs à lire:
  * **team_name**: Le champ du nom de l'équipe.
  * **name_n_relay**:Le nom du coureur du relais n.
  * **team_time**: Le temps passé en cumulé pour le marathon.
  * **time_n_relay**: Le temps effectué pour le relais.

A partir du document EKIDEN_TOULON/Resultats_ekiden_toulon.csv, le script *csv_reader.py* crée 3 fichiers csv:
* 5km.csv, qui rassemble les résultats triés de tous les concurrents ayant courus 5km (Relais 1, 3, 5)
* 10km.csv, qui rassemble les résultats triés de tous les concurrents ayant courus 10km (Relais 2 et 4)
* 7km.csv qui rassemble les résultats triés de tous les concurrents ayant courus 7km (Relais 6)

Dans l'exemple fourni, on peut voir les résultats de l'édition 2018 de l'ekiden de Toulon pour les coureurs du 5km.
```
Le premier relais est le plus rapide 39 fois
Le deuxième relais est le plus rapide 21 fois
Le troisième relais est le plus rapide 23 fois

Le premier relais est le deuxième plus rapide 26 fois
Le deuxième relais est le deuxième plus rapide 23 fois
Le troisième relais est le deuxième plus rapide 34 fois

Le premier relais est le plus lent 18 fois
Le deuxième relais est le plus lent 39 fois
Le troisième relais est le plus lent 26 fois

```


## Relais+duo
Le fichier analyze_duo.py lit le fichier csv indiqué dans *constantes.py* sous la variable "csv_duo" et va calculer le nombre de fois que:
* Le premier coureur est le plus rapide,
* Le deuxième coureur est le plus rapide,
* Les deux coureurs ont été aussi rapides.
Puis, on peut voir la moyenne de temps sur chaque boucle.

