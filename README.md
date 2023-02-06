
# TP Query ENSAI - Indexation Web

Ce mini-projet implémente une application répondant à une requête. Après quelques manipulations sur la requête, l'application cherche dans l'index tous les documents comportant tous les tokens de la requête.



## Authors

- [@tiroumalaifreddy](https://www.github.com/tiroumalaifreddy)


## Installation

Dans l'idéal, lancer un environnement virtuel (voir https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html).

Pour installer les packages requis:
```bash
pip install -r requirements.txt
```
    
## Usage/Examples

L'application prend en entrée:
- ```--json_file_doc {file_path_doc : str}````: permet d'indiquer le chemin du fichier json contenant la liste des documents avec l'id, l'URL et le titre du document
- ```--json_file_index {file_path_index : str}````: permet d'indiquer le chemin du fichier json contenant l'index

En se plaçant à la racine du projet et en ayant les deux fichiers à la racine du projet (```documents.json``` et ```index.json```):

```python
python3.8 main.py --json_file_doc documents.json --json_file_index index.json --query="Site Officiel" 
```

Un fichier json est alors crée à la racine:
-results.json : contient la liste des documents répondant à la requête avec le titre du document et l'URL associée.