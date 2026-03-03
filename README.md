# TOOLBOX
## Sphinx-Furo
### 1. Installation des dépendances

```powershell
uv add --dev furo myst_parser sphinxcontrib-bibtex

```

### 2. Initialisation

```powershell
mkdir docs
cd docs
uv run sphinx-quickstart
# Répondre aux questions (Projet, Nom, Version)
cd ..

```

### 3. Configuration (`docs/source/conf.py`)

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

extensions = [
    'sphinx.ext.autodoc',       # INDISPENSABLE : extrait la doc des docstrings
    'sphinx.ext.napoleon',      # Supporte le format Google/NumPy (plus lisible)
    'sphinx.ext.viewcode',      # Ajoute un lien [source] à côté de tes fonctions
    'sphinx.ext.mathjax',       # Pour le rendu des formules LaTeX
    'myst_parser',              # Pour lire les fichiers .md (README, etc.)
    'sphinxcontrib.bibtex',     # Pour la gestion du fichier .bib
]

html_theme = "furo"
bibtex_bibfiles = ['refs.bib']

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#7C4DFF",
        "color-brand-content": "#7C4DFF",
    },
}

```

### 4. Compilation

```powershell
uv run sphinx-build -b html docs/source public

```