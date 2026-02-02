"""Module providing the logic of the 2048 game"""

import random
import copy
from typing import List, Tuple

TAILLE:int = 4


# ==========================================================
# 🎯 FONCTION PUBLIQUE (API POUR L’INTERFACE)
# ==========================================================

def nouvelle_partie() -> Tuple[List[List[int]], int]:
    """
    Crée une nouvelle partie du jeu 2048.

    :return: Une grille TAILLExTAILLE initialisée avec deux tuiles, ainsi que le score à 0.
    :rtype: Tuple[List[List[int]], int]
    """
    plateau = _creer_plateau_vide()
    plateau = _ajouter_tuile(plateau)
    plateau = _ajouter_tuile(plateau)
    return (plateau, 0)

def jouer_coup(plateau: List[List[int]], direction: str) -> tuple[List[List[int]], int, bool]:
    """
    Effectuer un mouvement sur le plateau.

    :param plateau: Une grille TAILLExTAILLE du jeu.
    :type plateau: List[List[int]]
    :param direction: La direction du déplacement : 'g' (gauche), 'd' (droite), 'h' (haut), 'b' (bas).
    :type direction: str
    :return: Retourne un tuple (nouveau_plateau, points, est_fini).
    :rtype: tuple[List[List[int]], int, bool]
    """

    raise NotImplementedError("Fonction jouer_coup non implémentée.")

# ==========================================================
# 🔒 FONCTIONS PRIVÉES (LOGIQUE INTERNE)
# ==========================================================

def _creer_plateau_vide() -> List[List[int]]:
    """
    Crée une grille TAILLExTAILLE remplie de zéros.

    :return: Une grille vide.
    :rtype: List[List[int]]
    """
    return [[0 for _ in range(TAILLE)] for _ in range(TAILLE)]

def _get_cases_vides(plateau: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Retourne les coordonnées des cases vides sous forme d'une liste de coordonnées

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Une liste de coordonnées
    :rtype: List[Tuple[int, int]]
    """
    result = []
    for i in range(TAILLE):
        current=[(i,j) for j in range(TAILLE) if plateau[i][j]==0]
        for value in current:
            result.append(value)
    return result

def _ajouter_tuile(plateau: List[List[int]]) -> List[List[int]]:
    """
    Ajoute une tuile de valeur 2 sur une case vide.

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Une nouvelle grille avec une tuile ajoutée.
    :rtype: List[List[int]]
    """
    result = copy.deepcopy(plateau)
    case = random.choice(_get_cases_vides(result))
    result[case[0]][case[1]] = 2
    return result

def _supprimer_zeros(ligne: List[int]) -> List[int]:
    """
    Supprime les zéros d'une ligne.

    :param ligne: Une ligne de la grille.
    :type ligne: List[int]
    :return: La ligne sans zéros.
    :rtype: List[int]
    """
    return [v for v in ligne if v!=0]

def _fusionner(ligne: List[int]) -> Tuple[List[int], int]:
    """
    Fusionne les valeurs identiques consécutives d'une ligne.

    :param ligne: Une ligne sans zéros.
    :type ligne: List[int]
    :return: La ligne après fusion, les points gagnés
    :rtype: Tuple[List[int], int]
    """
    last = 0
    points = 0
    lenght = len(ligne)
    v = 0
    while v < lenght:
        if ligne[v] == last:
            points += ligne[v-1]*2
            ligne.insert(v-1, ligne[v-1]*2)
            ligne.pop(v)
            ligne.pop(v)
            last = 0
            lenght -= 1
        else:
            last = ligne[v]
            v += 1
    return (ligne, points)

def _completer_zeros(ligne: List[int]) -> List[int]:
    """
    Complète une ligne trop petite de zéros.

    :param ligne: Une ligne sans zéros.
    :type ligne: List[int]
    :return: La ligne après complétion.
    :rtype: List[int]
    """
    while len(ligne) < TAILLE:
        ligne.append(0)
    return ligne

def _deplacer_gauche(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Joue un coup à gauche sur une grille de jeu.

    :param plateau: Une grille de jeu.
    :type ligne: List[List[int]]
    :return: La grille après mouvement, les nouveau points.
    :rtype: Tuple[List[List[int]], int]
    """
    nouveaux_points = 0
    nouveau_plateau = []
    for l in plateau:
        l_sans_zero = _supprimer_zeros(l)
        l_fusionnee, points = _fusionner(l_sans_zero)
        nouveaux_points += points
        l_finale = _completer_zeros(l_fusionnee)
        nouveau_plateau.append(l_finale)
    return nouveau_plateau, nouveaux_points

def _inverser_lignes(plateau: List[List[int]]) -> List[List[int]]:
    """
    Inverse horizontalement chaque ligne d'une grille de jeu.

    :param plateau: Une grille de jeu.
    :type ligne: List[List[int]]
    :return: La grille inversion.
    :rtype: List[List[int]
    """
    nouveau_plateau = [v for v in plateau[::-1]]
    return nouveau_plateau

def _deplacer_droite(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers la droite en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :type plateau: List[List[int]]
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    :rtype: Tuple[List[List[int]], int]
    """
    raise NotImplementedError("Fonction _deplacer_droite non implémentée.")

def _transposer(plateau): # ajouter les annotations de type
    """
    DOCSTRING À ÉCRIRE
    """
    raise NotImplementedError("Fonction _transposer non implémentée.")

def _deplacer_haut(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers le haut en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    """
    raise NotImplementedError("Fonction _deplacer_haut non implémentée.")


def _deplacer_bas(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers le bas en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    """
    raise NotImplementedError("Fonction _deplacer_bas non implémentée.")

def _partie_terminee(plateau: List[List[int]]) -> bool:
    """
    DOCSTRING À ÉCRIRE
    """
    # Partie non terminee si il y a des cases vides
    # Partie non terminee si il y a des fusions possibles (horizontale ou verticale)
    # Sinon c'est vrai

    raise NotImplementedError("Fonction _partie_terminee non implémentée.")

#print()
