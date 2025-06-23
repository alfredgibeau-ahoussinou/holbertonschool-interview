# Array to AVL

## Contexte
Ce projet fait partie du cursus Holberton School et a pour objectif de manipuler les arbres binaires de recherche, plus précisément les arbres AVL, en C.

## Objectif du projet
Écrire une fonction qui construit un arbre AVL équilibré à partir d'un tableau trié d'entiers. L'arbre AVL est un arbre binaire de recherche auto-équilibré, garantissant des opérations efficaces.

## Structures de données utilisées
```c
/**
 * struct binary_tree_s - Noeud d'arbre binaire
 *
 * @n: Valeur entière stockée dans le noeud
 * @parent: Pointeur vers le parent
 * @left: Pointeur vers l'enfant gauche
 * @right: Pointeur vers l'enfant droit
 */
typedef struct binary_tree_s
{
    int n;
    struct binary_tree_s *parent;
    struct binary_tree_s *left;
    struct binary_tree_s *right;
} binary_tree_t;

typedef struct binary_tree_s avl_t;
```

## Prototype de la fonction
```c
avl_t *sorted_array_to_avl(int *array, size_t size);
```
- `array` : pointeur vers le premier élément du tableau trié
- `size` : nombre d'éléments dans le tableau
- Retourne un pointeur vers la racine de l'arbre AVL créé, ou NULL en cas d'échec

## Contraintes
- Pas de variables globales
- Maximum 3 fonctions par fichier
- Pas de rotations d'arbre
- Pas de valeurs dupliquées dans le tableau
- Respect du style Betty

## Exemple d'utilisation
```c
#include "binary_trees.h"

int main(void)
{
    avl_t *tree;
    int array[] = {1, 2, 20, 21, 22, 32, 34, 47, 62, 68, 79, 84, 87, 91, 95, 98};
    size_t n = sizeof(array) / sizeof(array[0]);

    tree = sorted_array_to_avl(array, n);
    // Affichage ou utilisation de l'arbre
    return (0);
}
```

## Explication de l'algorithme
L'algorithme consiste à :
1. Prendre l'élément du milieu du tableau comme racine (pour garantir l'équilibre)
2. Répéter récursivement pour la partie gauche (sous-arbre gauche) et droite (sous-arbre droit) du tableau
3. Relier chaque noeud à son parent

Ce procédé garantit que l'arbre est aussi équilibré que possible, car chaque sous-arbre est construit à partir de la moitié du tableau restant.

## Compilation et exécution
Pour compiler et exécuter :
```sh
gcc -Wall -Wextra -Werror -pedantic binary_tree_print.c 0-main.c 0-sorted_array_to_avl.c -o 0-sorted_array_to_avl
./0-sorted_array_to_avl
```

