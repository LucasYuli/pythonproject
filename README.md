# Gestionnaire de fichiers en Python du groupe 5

Ce projet consiste à créer une application en Python qui permet de gérer des fichiers texte. L'application utilise une classe `FileManager` pour lire, écrire, compter les lignes et rechercher des mots-clés dans un fichier texte. Le projet utilise aussi des modules externes gérés par `pip`.

## Installation des dépendances
1. Créez un environnement virtuel 
python3 -m venv CHEMINVERSLEVENV
exemple : python3 -m venv venv
Pour activer le venv: 
source venv/bin/activate

## Utilisation

1. Créez un fichier `log.txt` ou utilisez un fichier existant avec du contenu.

2. Modifiez le script Python principal pour indiquer le chemin du fichier que vous souhaitez gérer.

3. Exécutez le script Python pour tester les fonctionnalités :

    ```bash
    python gestionnaire_fichiers.py
    ```

    ## Fonctionnalités

La classe `FileManager` inclut les méthodes suivantes :

- `read_file()` : lit et affiche le contenu du fichier.
- `write_to_file(data)` : écrit des données à la fin du fichier.
- `count_lines()` : compte le nombre de lignes dans le fichier.
- `search_keyword(keyword)` : recherche un mot-clé dans le fichier et affiche les lignes correspondantes.

## Utilité du fichier requirements.txt

Le fichier `requirements.txt` contient la liste des dépendances nécessaires pour exécuter le projet. Il permet d'installer facilement toutes les bibliothèques requises avec la commande `pip install -r requirements.txt`. Cela garantit que le projet peut être exécuté dans un environnement contrôlé avec toutes les dépendances nécessaires.



    