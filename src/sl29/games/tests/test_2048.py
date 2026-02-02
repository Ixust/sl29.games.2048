"""Tests simples pour l'API publique du module 2048 (français)."""

from sl29.games._2048 import (  # type: ignore
    TAILLE,
    _creer_plateau_vide,
    _get_cases_vides,
    _ajouter_tuile,
    nouvelle_partie,
    _supprimer_zeros,
    _fusionner,
    _completer_zeros,
    _deplacer_gauche,
    _inverser_lignes,
    _deplacer_droite,
    _transposer,
    _deplacer_haut,
    _deplacer_bas,
    _partie_terminee,
    jouer_coup,
)

def test__creer_plateau_vide():
    print("----> Tests de _creer_plateau_vide...")
    plateau = _creer_plateau_vide()
    assert len(plateau) == TAILLE # 4 lignes
    for ligne in plateau:
        assert len(ligne) == TAILLE # 4 colonnes
        for valeur in ligne:
            assert valeur == 0, "chaque case devrait contenir 0." # toutes les cases à 0
    print("OK")

def test__get_cases_vides():
    print("----> Tests de _get_cases_vides...")
    plateau = [
        [0, 2, 4, 0],
        [2, 0, 8, 0],
        [2, 2, 2, 2],
        [8, 2, 4, 0],
    ]
    excepted = [(0,0),(0,3),(1,1),(1,3),(3,3)]
    result = _get_cases_vides(plateau)
    assert result == excepted, f"La fonction devrait retourner{excepted} mais retourne {result}"
    print("OK")


def test__ajouter_tuile():
    print("----> Tests de _ajouter_tuile...")
    plateau = _creer_plateau_vide()
    nouveau_plateau = _ajouter_tuile(plateau)
    # Vérifier qu'une seule tuile a été ajoutée
    compte_tuiles = 0
    for ligne in nouveau_plateau:
        for valeur in ligne:
            if valeur == 2:
                compte_tuiles += 1
    assert compte_tuiles == 1, "Une seule tuile de valeur 2 devrait être ajoutée."
    assert plateau != nouveau_plateau, "Le plateau original ne doit pas être modifié"

    plateau_non_vide = [
        [2, 0, 0, 0],
        [0, 4, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    nouveau_plateau2 = _ajouter_tuile(plateau_non_vide)
    # Vérifier qu'une seule tuile a été ajoutée
    compte_tuiles2 = 0
    for ligne in nouveau_plateau2:
        for valeur in ligne:
            if valeur == 2:
                compte_tuiles2 += 1
    assert compte_tuiles2 == 2, "Il devrait y avoir deux tuiles de valeur 2 au total."
    assert plateau_non_vide != nouveau_plateau2, "Le plateau original ne doit pas être modifié"
    print("OK")

def test__supprimer_zeros():
    print("----> Tests de _supprimer_zeros...")
    ligne = [2, 0, 0, 0]
    excepted = [2]
    result = _supprimer_zeros(ligne)
    assert excepted == result, f"La fonction devrait retourner{excepted} mais retourne {result}"
    print("OK")

def test__fusionner():
    print("----> Tests de _fusionner...")
    inputs_expecteds = (
        ([], ([], 0)),
        ([2], ([2], 0)),
        ([2, 2], ([4], 4)),
        ([2, 2, 2], ([4, 2], 4)),
        ([2, 2, 2, 2], ([4, 4], 8)),
        ([4, 4, 8, 8], ([8, 16], 24)),
        ([2, 4, 4, 2], ([2, 8, 2], 8)),
        ([2, 2, 4, 4, 8], ([4, 8, 8], 12)),
    )
    for inp, expected in inputs_expecteds:
        result, points = _fusionner(inp)
        assert result == expected[0], f"Pour l'entrée {inp}, attendu {expected[0]} mais obtenu {result}."
        assert points == expected[1], f"Pour l'entrée {inp}, J'aurais du  avoir {expected[1]} points mais j'ai obtenu {points} points."
    print("OK")

def test__completer_zeros():
    print("----> Tests de _completer_zeros...")
    inputs_expecteds = (
        ([], [0,0,0,0]),
        ([2], [2,0,0,0]),
        ([2, 2], [2,2,0,0]),
        ([2, 2, 2], [2, 2, 2,0]),
        ([2, 2, 2, 2], [2, 2, 2, 2]),
    )
    for inp, expected in inputs_expecteds:
        result = _completer_zeros(inp)
        assert result == expected, f"Pour l'entrée {inp}, attendu {expected} mais obtenu {result}"
    print("OK")

def test_nouvelle_partie():
    print("----> Tests de nouvelle_partie...")
    plateau, score = nouvelle_partie()
    compte_tuiles = 0
    for ligne in plateau:
        for valeur in ligne:
            if valeur == 2:
                compte_tuiles += 1
    assert compte_tuiles == 2, "Une nouvelle partie doit commencer avec deux tuiles de valeur 2."
    assert score == 0, "Une nouvelle partie doit commencer avec un score à 0."
    print("OK")

def test__deplacer_gauche():
    print("----> Tests de _deplacer_gauche...")
    plateau = [
        [2, 2, 0, 0],
        [2, 2, 2, 2],
        [0, 0, 4, 4],
        [8, 4, 2, 2]
    ]
    # Rappel : [2,2,2,2] -> [4,4,0,0] (8 pts)
    # [8,4,2,2] -> [8,4,4,0] (4 pts)
    attendu_p = [
        [4, 0, 0, 0],
        [4, 4, 0, 0],
        [8, 0, 0, 0],
        [8, 4, 4, 0]
    ]
    attendu_pts = 4 + 8 + 8 + 4 # 24 points

    resultat, points = _deplacer_gauche(plateau)
    assert resultat == attendu_p
    assert points == attendu_pts
    print("OK")

def test__inverser_lignes():
    print("----> Tests de _inverser_lignes...")
    raise NotImplementedError("Tests de _inverser_lignes non implémentés.")
    print("OK")

def test__deplacer_droite():
    print("----> Tests de _deplacer_droite...")
    raise NotImplementedError("Tests de _deplacer_droite non implémentés.")
    print("OK")

def test__transposer():
    print("----> Tests de _transposer...")
    raise NotImplementedError("Tests de _transposer non implémentés.")
    print("OK")

def test__deplacer_haut():
    print("----> Tests de _deplacer_haut...")
    raise NotImplementedError("Tests de _deplacer_haut non implémentés.")
    print("OK")

def test__deplacer_bas():
    print("----> Tests de _deplacer_bas...")
    plateau = [
        [2, 2, 0, 8],
        [2, 0, 4, 4],
        [0, 2, 4, 2],
        [0, 2, 0, 2]
    ]
    attendu_p = [
        [0, 0, 0, 0],
        [0, 0, 0, 8],
        [0, 2, 0, 4],
        [4, 4, 8, 4]
    ]
    resultat, points = _deplacer_bas(plateau)
    assert resultat == attendu_p, f"J'aurais du avoir ce plateau {attendu_p} points mais j'ai ce plateau {resultat}."
    assert points == 20, f"J'aurais du avoir {20} points mais j'ai {points} points."
    print("OK")

def test_jouer_coup():
    print("----> Tests de jouer_coup...")

    # --- Cas 1 : Le mouvement est possible ---
    # Un plateau avec un seul 2 à gauche.
    plateau_init = [
        [2, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    # Si on joue à droite, le 2 doit bouger, donc une nouvelle tuile doit apparaître.
    nouveau, points, _ = jouer_coup(plateau_init, "d")

    compte = sum(1 for ligne in nouveau for v in ligne if v > 0)
    assert compte == 2, f"Une nouvelle tuile aurait dû apparaître. Attendu 2 tuiles, obtenu {compte}"
    assert nouveau[0][3] == 2, "Le 2 initial aurait dû se déplacer à l'indice [0][3]"
    assert points == 0, "Aucune fusion, les points devraient être à 0"

    # --- Cas 2 : Le mouvement est impossible ---
    plateau_bloque = [
        [2, 4, 8, 16],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    # On essaie de jouer à gauche (déjà collé). Rien ne doit changer, aucune tuile ajoutée.
    nouveau2, _, _ = jouer_coup(plateau_bloque, "g")

    assert nouveau2 == plateau_bloque, "Le plateau ne devrait pas avoir changé"
    compte2 = sum(1 for ligne in nouveau2 for v in ligne if v > 0)
    assert compte2 == 4, "Aucune tuile ne doit être ajoutée si le mouvement n'a rien déplacé"

    # --- Cas 3 : déplacement bas ---
    plateau = [
        [2, 2, 4, 8],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    nouveau3, _, _ = jouer_coup(plateau, "b")
    expected = [2, 2, 4, 8]
    assert expected == nouveau3[3], f"La derniere ligne aurait du être {expected} mais vaut {nouveau3[3]}."

    # --- Cas 4 : Déplacement en bas ---
    plateau_fusion = [
        [2, 2, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    _, points3, _ = jouer_coup(plateau_fusion, "g")
    assert points3 == 4, f"La fusion 2+2 aurait dû rapporter 4 points, obtenu {points3}"

    # --- Cas 5 : Fin de partie ---
    # Un plateau plein sans aucune fusion possible
    plateau_plein = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2]
    ]
    _, _, fini_partie = jouer_coup(plateau_plein, "h")
    assert fini_partie is True, "La partie devrait être déclarée terminée (fini=True)"

    print("OK")

def test__partie_terminee():
    print("----> Tests de _partie_terminee...")

    # Cas 1 : La partie n'est pas finie car il reste des cases vides
    plateau_vide = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 0, 2]  # Un zéro ici
    ]
    assert _partie_terminee(plateau_vide) is False, "Il reste un 0, la partie ne devrait pas être finie."

    # Cas 2 : Le plateau est plein mais une fusion HORIZONTALE est possible
    plateau_fus_h = [
        [2, 4, 2, 4],
        [4, 2, 2, 8], # Deux '2' côte à côte
        [2, 4, 8, 2],
        [4, 2, 4, 8]
    ]
    assert _partie_terminee(plateau_fus_h) is False, "Fusion horizontale possible en ligne 2."

    # Cas 3 : Le plateau est plein mais une fusion VERTICALE est possible
    plateau_fus_v = [
        [2, 4, 2, 4],
        [4, 8, 4, 2],
        [2, 8, 2, 4], # Deux '8' l'un au-dessus de l'autre
        [4, 2, 4, 2]
    ]
    assert _partie_terminee(plateau_fus_v) is False, "Fusion verticale possible en colonne 2."

    # Cas 4 : La partie est VRAIMENT finie
    plateau_bloque = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2]
    ]
    assert _partie_terminee(plateau_bloque) is True, "Aucun mouvement possible, la partie devrait être finie."

    print("OK")

def main():
    test__creer_plateau_vide()
    test__get_cases_vides()
    test__ajouter_tuile()
    test__supprimer_zeros()
    test__fusionner()
    test__completer_zeros()
    test_nouvelle_partie()
    test__deplacer_gauche()
    test__inverser_lignes()
    test__deplacer_droite()
    test__transposer()
    test__deplacer_haut()
    test__deplacer_bas()
    test_jouer_coup()
    test__partie_terminee()

def test_jouer_coup_direction_invalide():
    print("----> Tests de jouer_coup avec direction invalide...")
    plateau = [[2,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    nouveau, points, fini = jouer_coup(plateau, "x")
    assert nouveau == plateau
    assert points == 0
    assert fini == False
    print("OK")

def test_ajouter_tuile_plein():
    print("----> Tests de _ajouter_tuile sur plateau plein...")
    plateau = [[2,4,8,16],[32,64,128,256],[512,1024,2048,4096],[8192,16384,32768,65536]]
    nouveau = _ajouter_tuile(plateau)
    assert nouveau == plateau  # pas de changement car plein
    print("OK")

def test_partie_terminee_avec_fusions():
    print("----> Tests de _partie_terminee avec fusions possibles...")
    # Horizontal
    plateau = [[2,2,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    assert _partie_terminee(plateau) == False
    # Vertical
    plateau = [[2,0,0,0],[2,0,0,0],[0,0,0,0],[0,0,0,0]]
    assert _partie_terminee(plateau) == False
    print("OK")

def test_partie_terminee_plein_sans_fusions():
    print("----> Tests de _partie_terminee plateau plein sans fusions...")
    plateau = [[2,4,8,16],[32,64,128,256],[512,1024,2048,4096],[8192,16384,32768,65536]]
    assert _partie_terminee(plateau) == True
    print("OK")

if __name__ == "__main__":
	main()
