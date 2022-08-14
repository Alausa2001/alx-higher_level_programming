#include "lists.h"
/**
 * insert_node - it inserts a number into a sorted list
 * @head: pointer to the head of the list
 * @number: number to insert
 * Return: the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = *head;
	listint_t *current = *head;
	listint_t *store = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL)
		*head = newnode;
	else
	{
		if (current->n > number)
		{
			*head = newnode;
			newnode->next = store;

		}
		while (current->next != NULL && current->next->n < number)
			current = current->next;
		newnode->next = current->next;
		current->next = newnode;
	}
	return (newnode);
}
