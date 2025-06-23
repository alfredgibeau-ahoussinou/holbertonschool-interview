# Problème des N reines

Ce projet résout le problème classique des N reines : placer N reines sur un échiquier de taille N×N de sorte qu'aucune reine ne puisse en attaquer une autre (aucune sur la même ligne, colonne ou diagonale).

## Fichiers
- `0-nqueens.py` : Script principal pour résoudre le problème.

## Utilisation

```bash
./0-nqueens.py N
```
- `N` doit être un entier supérieur ou égal à 4.

### Exemples
```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Gestion des erreurs
- Si le nombre d'arguments est incorrect :
  - Affiche `Usage: nqueens N` et quitte avec le code 1.
- Si `N` n'est pas un nombre :
  - Affiche `N must be a number` et quitte avec le code 1.
- Si `N` < 4 :
  - Affiche `N must be at least 4` et quitte avec le code 1.

## Explication du code

Le script utilise une approche de **backtracking** (retour sur trace) pour explorer toutes les positions possibles des reines.

### Fonctions principales :
- `is_safe(board, row, col, N)` :
  - Vérifie si une reine peut être placée à la ligne `row` et colonne `col` sans être attaquée par une autre reine déjà placée.
  - Elle vérifie la colonne et les deux diagonales.

- `solve_n_queens(N)` :
  - Lance la résolution pour un échiquier de taille `N`.
  - Utilise une fonction interne `backtrack(queens, row)` pour placer les reines ligne par ligne.
  - `queens` est une liste où l'indice représente la ligne et la valeur la colonne de la reine.
  - Si une solution est trouvée, elle est ajoutée à la liste des solutions.

- La boucle principale vérifie les arguments, convertit `N` en entier, puis affiche toutes les solutions trouvées sous forme de liste de coordonnées `[ligne, colonne]`.

## Exemple de solution pour N=4
Pour N=4, il y a 2 solutions possibles :
- `[[0, 1], [1, 3], [2, 0], [3, 2]]`
- `[[0, 2], [1, 0], [2, 3], [3, 1]]`

Chaque sous-liste `[i, j]` indique qu'une reine est placée à la ligne `i` et colonne `j`.

## Auteur
Projet réalisé par Holberton School.
