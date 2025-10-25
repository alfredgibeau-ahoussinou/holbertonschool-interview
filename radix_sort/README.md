# Radix Sort

## Description

Ce projet implémente l'algorithme de tri par base (Radix Sort) en utilisant l'approche LSD (Least Significant Digit). L'algorithme trie un tableau d'entiers dans l'ordre croissant en utilisant le tri par comptage comme sous-routine.

## Algorithme

Le Radix Sort fonctionne en triant les nombres chiffre par chiffre, en commençant par le chiffre le moins significatif (unités) jusqu'au chiffre le plus significatif. Pour chaque position de chiffre, il utilise le tri par comptage (counting sort) pour maintenir l'ordre relatif des éléments.

### Étapes de l'algorithme :

1. **Trouver le maximum** : Détermine la valeur maximale dans le tableau pour connaître le nombre de chiffres à traiter
2. **Tri par position** : Pour chaque position de chiffre (1, 10, 100, ...) :
   - Utilise le tri par comptage pour trier selon cette position
   - Affiche le tableau après chaque étape de tri
3. **Résultat** : Le tableau est complètement trié après avoir traité tous les chiffres

## Complexité

- **Complexité temporelle** : O(d × (n + k))
  - n = nombre d'éléments
  - k = base (10 pour les entiers décimaux)
  - d = nombre de chiffres du nombre maximum
- **Complexité spatiale** : O(n + k)
- **Stabilité** : Oui, l'algorithme est stable

## Fichiers

### `0-radix_sort.c`
Contient l'implémentation principale de l'algorithme avec trois fonctions :

- `get_max()` : Trouve la valeur maximale dans le tableau
- `counting_sort()` : Effectue le tri par comptage sur une position de chiffre donnée
- `radix_sort()` : Fonction principale qui orchestre le tri par base

### `0-main.c`
Programme de test qui :
- Initialise un tableau d'entiers
- Affiche le tableau non trié
- Exécute le tri par base
- Affiche le tableau trié

### `print_array.c`
Fonction utilitaire pour afficher un tableau d'entiers de manière formatée.

### `sort.h`
Fichier d'en-tête contenant les prototypes des fonctions.

## Compilation et exécution

```bash
gcc -Wall -Wextra -Werror -pedantic -std=gnu89 *.c -o radix
```

```bash
./radix
```

## Exemple d'exécution

```
19, 48, 99, 71, 13, 52, 96, 73, 86, 7

7, 48, 71, 13, 52, 73, 86, 96, 19, 99
7, 13, 19, 48, 52, 71, 73, 86, 96, 99

7, 13, 19, 48, 52, 71, 73, 86, 96, 99
```

## Fonctionnalités

- ✅ Tri par base LSD (Least Significant Digit)
- ✅ Tri par comptage comme sous-routine
- ✅ Affichage du tableau après chaque étape de tri
- ✅ Gestion des tableaux de taille 1 ou 0
- ✅ Allocation dynamique de mémoire
- ✅ Libération appropriée de la mémoire
- ✅ Code documenté selon le style de documentation C

## Avantages du Radix Sort

1. **Performance linéaire** : Complexité temporelle O(d × (n + k)) qui peut être très efficace
2. **Stabilité** : Maintient l'ordre relatif des éléments égaux
3. **Pas de comparaisons** : N'utilise pas de comparaisons entre éléments
4. **Prévisible** : Performance constante indépendamment de la distribution des données

## Limitations

1. **Espace mémoire** : Nécessite de l'espace supplémentaire pour le tri par comptage
2. **Entiers uniquement** : Fonctionne principalement avec des entiers non négatifs
3. **Base fixe** : Optimisé pour la base 10 (chiffres décimaux)

## Auteur

Projet réalisé dans le cadre de Holberton School.
