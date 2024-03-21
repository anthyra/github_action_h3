import random

def calculer_moyenne(liste):
    if len(liste) == 0:
        return 0  # Si la liste est vide, retourner 0
    somme = sum(liste)
    moyenne = somme / len(liste)
    return moyenne

# Générer une liste de 10 nombres aléatoires entre 1 et 100
ma_liste = [random.randint(1, 100) for _ in range(10)]

print("La liste générée est :", ma_liste)

# Calculer la moyenne des nombres dans la liste
resultat = calculer_moyenne(ma_liste)
print("La moyenne est :", resultat)
