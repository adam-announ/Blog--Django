# 📝 Blog--Django

Un projet de blog développé avec le framework **Django**, visant à explorer ses fonctionnalités tout en construisant une plateforme complète de publication d'articles.

## 🚀 Objectifs du projet

- Apprendre les fondamentaux de Django : modèles, vues, templates, forms, admin, etc.
- Implémenter une interface utilisateur intuitive pour lire, écrire et gérer des articles.
- Ajouter des fonctionnalités avancées comme les commentaires, les tags, la recherche, la pagination et l’authentification.

## 🛠️ Fonctionnalités

- ✅ Création, édition et suppression d’articles de blog
- ✅ Interface d’administration Django personnalisée
- ✅ Authentification des utilisateurs (connexion, inscription, déconnexion)
- ✅ Gestion des commentaires
- ✅ Catégorisation et tags des articles
- ✅ Moteur de recherche intégré
- ✅ Pagination des articles
- ✅ Slug SEO-friendly pour les URLs
- ✅ Système de brouillons et de publications différées

## 📦 Stack technique

- **Backend** : Django (Python)
- **Base de données** : SQLite (ou PostgreSQL en production)
- **Frontend** : HTML5, CSS3 (Bootstrap), Django Templates
- **Autres outils** :
  - Django Crispy Forms
  - Django Taggit (pour la gestion des tags)
  - Django Debug Toolbar (pour le débogage)

## 🧰 Installation locale

### 1. Cloner le dépôt

```bash
git clone https://github.com/ton-utilisateur/Blog--Django.git
cd Blog--Django
```

### 2. Créer un environnement virtuel

```bash
python -m venv env
source env/bin/activate  # Sous Windows : env\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations

```bash
python manage.py migrate
```

### 5. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur de développement

```bash
python manage.py runserver
```

Puis accéder au site sur : `http://127.0.0.1:8000/`

## 🧪 Tests

Lancer les tests avec :

```bash
python manage.py test
```

## 📁 Structure du projet

```bash
Blog--Django/
├── blog/                # App principale : gestion des articles
├── accounts/            # App secondaire : gestion des utilisateurs
├── static/              # Fichiers CSS/JS
├── templates/           # Templates HTML
├── media/               # Fichiers uploadés
├── manage.py
├── db.sqlite3
└── requirements.txt
```

## 🔒 Sécurité & bonnes pratiques

- Fichiers sensibles comme `.env` sont exclus via `.gitignore`
- Utilisation de variables d’environnement pour les clés secrètes
- Séparation des paramètres de développement et de production

## 🗺️ Roadmap (prochaines fonctionnalités)

- [ ] Système de likes / réactions
- [ ] Système de notifications
- [ ] Interface utilisateur responsive améliorée
- [ ] Support de Markdown dans les articles
- [ ] API REST (avec Django REST Framework)

## 🤝 Contribuer

Les contributions sont les bienvenues ! N’hésitez pas à :

- Ouvrir une *issue*
- Soumettre une *pull request*
- Suggérer des améliorations


---

**Développé avec ❤️ par [AKERT]**
