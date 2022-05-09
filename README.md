## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Disclaimer

Le projet étant à un stade embryonnaire les bonnes pratiques propres au déploiement d'un projet django n'ont pas toutes été respectées (gestion des staticfiles et serveur webs par défaut, utilisation de sqlite).

### Usage

Le déploiement s'effectue lorsque la branche `master` du projet est modifiée, l'orchestrateur de *CircleCI* déclenche alors un pipeline comportant les étapes suivantes:

1. Installation des dépendances du projet et mise en oeuvre des tests unitaires
2. Conteneurisation de l'application
3. Publication de l'artefact sur Docker Hub / déploiement vers heroku 

Note: L'étape 2 dépend de la réussite de l'étape 1, de même l'étape 3 dépend de la réussite de l'étape 2.

### Mise en place

Le projet a été configuré pour être déployé sur la plateforme heroku via un pipeline CircleCI, voir le fichier `.circleci/config.yml`, une journalisation des erreurs de l'application est également mise en place avec Sentry (voir `config/setting.py`), de plus chaque artefact est publié sur Docker Hub.

La configuration sur heroku nécessite seulement la création d'une app.

Pour utiliser le pipeline il suffit de configurer un nouveau projet dans l'interface de CircleCI avec le lien du repository souhaité. A noter qu'il sera nécessaire de configurer les variables d'environnement suivantes:

* `DOCKERHUB_PASSWORD`
* `DOCKERHUB_TOKEN`
* `DOCKERHUB_USERNAME`
* `HEROKU_API_KEY`
* `HEROKU_APP_NAME`
* `HEROKU_LOGIN`
* `HEROKU_REGISTRY`

La journalisation des erreurs nécessite un lien DSN (data source name), celui-ci n'est pas spécifié dans le fichier `config/settings.py`, le SDK de Sentry cherchera donc une variable d'environnement `SENTRY_DSN` à configurer sur heroku.
