#include "lists.h"

/**
 * insert_node - FUNCTION
 * @head: pointer
 * @number: number
 * Return:pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nod = *head, *new1;

	new1 = malloc(sizeof(listint_t));
	if (new1 == NULL)
		return (NULL);
	new1->n = number;

	if (nod == NULL || nod->n >= number)
	{
		new1->next = nod;
		*head = new1;
		return (new1);
	}

	while (nod && nod->next && nod->next->n < number)
		nod = nod->next;

	new1->next = nod->next;
	nod->next = new1;

	return (new1);
}
