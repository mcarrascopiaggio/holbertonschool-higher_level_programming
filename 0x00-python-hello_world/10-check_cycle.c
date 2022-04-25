#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function in C that checks if a SLL has a cycle in it
 * @list: pointer to the list tha we will check
 * Return:0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *one = list;
	listint_t *doble = list;

	if (list == NULL)
		return (0);
	while (doble && doble->next)
	{
		one = one->next;
		doble = doble->next->next;
		if (one == doble)
			return (1);
	}
return (0);
}
