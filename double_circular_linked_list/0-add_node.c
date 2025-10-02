#include <stdlib.h>
#include <string.h>
#include "list.h"

/**
 * add_node_end - Add a new node to the end of a double circular linked list
 * @list: the list to modify
 * @str: the string to copy into the new node
 *
 * Return: Address of the new node, or NULL on failure
 */
List *add_node_end(List **list, char *str)
{
    List *new_node, *current;

    if (!list || !str)
        return (NULL);

    /* Create new node */
    new_node = malloc(sizeof(List));
    if (!new_node)
        return (NULL);

    new_node->str = strdup(str);
    if (!new_node->str)
    {
        free(new_node);
        return (NULL);
    }

    /* If list is empty */
    if (!*list)
    {
        new_node->prev = new_node;
        new_node->next = new_node;
        *list = new_node;
        return (new_node);
    }

    /* Find the last node (the one before the head) */
    current = *list;
    while (current->next != *list)
        current = current->next;

    /* Insert new node at the end */
    new_node->prev = current;
    new_node->next = *list;
    current->next = new_node;
    (*list)->prev = new_node;

    return (new_node);
}

/**
 * add_node_begin - Add a new node to the beginning of a double circular linked list
 * @list: the list to modify
 * @str: the string to copy into the new node
 *
 * Return: Address of the new node, or NULL on failure
 */
List *add_node_begin(List **list, char *str)
{
    List *new_node, *current;

    if (!list || !str)
        return (NULL);

    /* Create new node */
    new_node = malloc(sizeof(List));
    if (!new_node)
        return (NULL);

    new_node->str = strdup(str);
    if (!new_node->str)
    {
        free(new_node);
        return (NULL);
    }

    /* If list is empty */
    if (!*list)
    {
        new_node->prev = new_node;
        new_node->next = new_node;
        *list = new_node;
        return (new_node);
    }

    /* Insert new node at the beginning */
    current = *list;
    new_node->prev = current->prev;
    new_node->next = current;
    current->prev->next = new_node;
    current->prev = new_node;
    *list = new_node;

    return (new_node);
}
