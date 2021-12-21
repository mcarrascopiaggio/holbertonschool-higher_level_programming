#include "lists.h"

/**
 *check_cycle - check if a linked list have a loop
 *@list: linked list to be checked
 *Return: 1 o 0
 */

int check_cycle(listint_t *list)
{
listint_t *node1 = list;
listint_t *node2 = list;

if (!list)
	return (0);

while (node2 && node2->next)
{
node1 = node1->next;
node2 = node2->next->next;

if (node1 == node2)
	return (1);
}
return (0);
}

