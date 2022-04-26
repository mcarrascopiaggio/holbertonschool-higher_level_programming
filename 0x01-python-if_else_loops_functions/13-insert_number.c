#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: linked list
 * @number: number ti be insert
 * Return:the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *temp = NULL;
	listint_t *aux = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
	{
		free(new);
		return (NULL);
	}
	new->n = number;/** node created with number inserted*/
	if (!*head)
		return (*head = new);/** case no list*/
	if (number <= (*head)->n)/**case first place*/
	{
		new->next = *head;
		return (*head = new);
	}
	temp = *head;
	aux  = temp->next;
	while (aux)
	{
		if (aux->n >= number) /**go until the next number be bigger*/
			break;
		temp = aux;/** node goes before*/
		aux = aux->next;
	}
	temp->next = new;
	new->next = aux;
	return (new);
}
