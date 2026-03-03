import pandas as pd
import pytest
from app.modules.mon_module import add, print_data, square, sub


# Fixture pour un DataFrame simple
@pytest.fixture
def sample_dataframe():
    """Crée un DataFrame Pandas simple pour les tests."""
    data = {"col1": [1, 2, 3], "col2": [4, 5, 6]}
    return pd.DataFrame(data)


# Tests pour la fonction add
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (10.5, 2.5, 13.0),
    ],
)
def test_add(a, b, expected):
    """Teste la fonction add avec différentes valeurs."""
    assert add(a, b) == expected


# Tests pour la fonction sub
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (1, 1, 0),
        (0, 5, -5),
        (10.5, 2.5, 8.0),
    ],
)
def test_sub(a, b, expected):
    """Teste la fonction sub avec différentes valeurs."""
    assert sub(a, b) == expected


# Tests pour la fonction square
@pytest.mark.parametrize(
    "a, expected",
    [
        (2, 4),
        (-3, 9),
        (0, 0),
        (1.5, 2.25),
    ],
)
def test_square(a, expected):
    """Teste la fonction square avec différentes valeurs."""
    assert square(a) == expected


# Test pour la fonction print_data
def test_print_data(sample_dataframe, capsys):
    """Teste la fonction print_data en capturant la sortie standard
    et en vérifiant le nombre de lignes retourné.
    """
    expected_rows = len(sample_dataframe)
    returned_rows = print_data(sample_dataframe)

    # Vérifie que le DataFrame a bien été affiché
    captured = capsys.readouterr()
    assert sample_dataframe.to_string() in captured.out

    # Vérifie que le nombre de lignes retourné est correct
    assert returned_rows == expected_rows


# Test pour la lecture du CSV et son traitement par la fonction print_data
def test_process_csv_data(sample_dataframe, capsys):
    """Teste le processus de lecture d'un CSV et son affichage via print_data."""
    # On simule la présence du fichier moncsv.csv dans le répertoire courant
    # Pour cela, on peut directement utiliser le DataFrame généré par la fixture
    # comme si c'était le contenu lu du CSV.
    # Si vous aviez un vrai fichier, vous utiliseriez pd.read_csv('app/moncsv.csv')

    expected_rows = len(sample_dataframe)
    returned_rows = print_data(sample_dataframe)  # Utilisation directe du DataFrame

    captured = capsys.readouterr()
    assert sample_dataframe.to_string() in captured.out
    assert returned_rows == expected_rows
