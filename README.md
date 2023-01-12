# Musask

Application Flask connecté à ElasticSearch pour rechercher des musées.

## Lignes de commande

**Créer le mapping pour les musées**

curl -H 'Content-Type: application/json' -XPUT http://localhost:9200/musee?pretty -d @data/musee/mapping.json

**Remplir l'index de données**

curl -H "Content-Type: application/json" -XPOST http://localhost:9200/_bulk --data-binary @data/musee/data.json

## TODO

- Mettre en place une meilleure recherche
- Mettre en place un système de pagination
- Ajouter Leaflet
- Ajouter un système CRUD
- Ajouter Kibana