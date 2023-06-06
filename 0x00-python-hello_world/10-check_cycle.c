#include "lists.h"

/**
 * check_cycle - checks if a code has cycle
 *
 * @head: the head of the linked list
 *
 * Return: 1 if cycle exit and 1 otherwise
 */



int check_cycle(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head->next;

	if (slow == NULL || fast == NULL)
	{
		return (0);
	}
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{

		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
