#include "lists.h"

/**
 * is_palindrome - function
 * @head:head address
 * Return: 1 or 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *pointer = *head;
	int tab[2048], i = 0, j = 0;

	if (*head)
	{
		while (pointer)
		{
			tab[i] = pointer->n;
			pointer = pointer->next;
			i++;
		}

		while (j < i / 2)
		{
			if (tab[j] == tab[i - j - 1])
				j++;
			else
				return (0);
		}
	}
	return (1);
}
