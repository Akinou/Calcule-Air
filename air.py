import math

def aire_carre(cote):
    """Calcule l'aire d'un carré de côté cote."""
    return cote ** 2

def aire_rectangle(longueur, largeur):
    """Calcule l'aire d'un rectangle de longueur longueur et de largeur largeur."""
    return longueur * largeur

def aire_triangle(base, hauteur):
    """Calcule l'aire d'un triangle de base base et de hauteur hauteur."""
    return (base * hauteur) / 2

def aire_cercle(rayon):
    """Calcule l'aire d'un cercle de rayon rayon."""
    return math.pi * rayon ** 2

def aire_parallelogramme(base, hauteur):
    """Calcule l'aire d'un parallélogramme de base base et de hauteur hauteur."""
    return base * hauteur

def aire_trapeze(base1, base2, hauteur):
    """Calcule l'aire d'un trapèze de bases base1 et base2 et de hauteur hauteur."""
    return (base1 + base2) * hauteur / 2

def aire_losange(diagonale1, diagonale2):
    """Calcule l'aire d'un losange de diagonales diagonale1 et diagonale2."""
    return diagonale1 * diagonale2 / 2

# Exemple d'utilisation :
cote = 5
longueur = 8
largeur = 3
base = 6
hauteur = 4
rayon = 2
base_parallelogramme = 5
hauteur_parallelogramme = 3
base1_trapeze = 5
base2_trapeze = 7
hauteur_trapeze = 4
diagonale1_losange = 6
diagonale2_losange = 8

aire_du_carre = aire_carre(cote)
aire_du_rectangle = aire_rectangle(longueur, largeur)
aire_du_triangle = aire_triangle(base, hauteur)
aire_du_cercle = aire_cercle(rayon)
aire_du_parallelogramme = aire_parallelogramme(base_parallelogramme, hauteur_parallelogramme)
aire_du_trapeze = aire_trapeze(base1_trapeze, base2_trapeze, hauteur_trapeze)
aire_du_losange = aire_losange(diagonale1_losange, diagonale2_losange)

print(f"L'aire du carré de côté {cote} est {aire_du_carre}")
print(f"L'aire du rectangle de longueur {longueur} et de largeur {largeur} est {aire_du_rectangle}")
print(f"L'aire du triangle de base {base} et de hauteur {hauteur} est {aire_du_triangle}")
print(f"L'aire du cercle de rayon {rayon} est {aire_du_cercle}")
print(f"L'aire du parallélogramme de base {base_parallelogramme} et de hauteur {hauteur_parallelogramme} est {aire_du_parallelogramme}")
print(f"L'aire du trapèze de bases {base1_trapeze} et {base2_tr
