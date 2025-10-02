# Double Circular Linked List

This project implements two functions to manage a double circular linked list of strings.

## Data structure

```c
/**
 * struct List - doubly linked list
 * @str: string - (malloc'ed string)
 * @prev: points to the previous node
 * @next: points to the next node
 */
typedef struct List
{
    char *str;
    struct List *prev;
    struct List *next;
} List;
```

## Functions

- `List *add_node_end(List **list, char *str);`
  - Adds a new node to the end of a double circular linked list.
  - Returns the address of the new node, or `NULL` on failure.

- `List *add_node_begin(List **list, char *str);`
  - Adds a new node to the beginning of a double circular linked list.
  - Returns the address of the new node, or `NULL` on failure.

## Compilation

Use the following flags:

```bash
gcc -Wall -Wextra -Werror -pedantic 0-add_node.c
```

Only the following C standard library functions are allowed: `malloc`, `free`, `strdup`.

## Files

- `0-add_node.c`: Implementation of the required functions.
- `list.h`: Header with the `List` type and function prototypes.
- `README.md`: Project description.

