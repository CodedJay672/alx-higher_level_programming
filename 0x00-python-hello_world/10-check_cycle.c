#include "lists.h"

/**
 * check_cycle -> funct that checks if a linked list
 * contains a loop
 * @list: pointer to the linked list
 * Return: return 1 if loop is detected else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_p = list, *fast_p = list;

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
			return (1);
	}
	return (0);
}
