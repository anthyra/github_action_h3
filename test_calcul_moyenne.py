import pytest
from job import calculer_moyenne

def test_calcul_moyenne():
    # Test avec une liste non vide
    assert calculer_moyenne([1, 2, 3, 4, 5]) == 3.0

    # Test avec une liste vide
    assert calculer_moyenne([]) == 0

    # Test avec une liste contenant un seul élément
    assert calculer_moyenne([10]) == 10.0

    # Test avec une liste de nombres négatifs
    assert calculer_moyenne([-1, -2, -3, -4, -5]) == -3.0

if __name__ == "__main__":
    pytest.main()
