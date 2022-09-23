#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node -> funct that inserts node in a sorted linked list
 * @head: pointer to the head node
 * @number: parameter for the number variable of the node
 * Return: returns address of the new node or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *prev = *head;
	listint_t *next = prev->next;

	temp = (listint_t *)malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		temp->next = NULL;
		*head = temp;
		return (temp);
	}
	while (next != NULL)
	{
		if (next->n > number)
		{
			temp->next = next;
			prev->next = temp;
			return (temp);
		}
		prev = next;
		next = prev->next;
	}
	temp->next = next;
	prev->next = temp;
	return (temp);
}
