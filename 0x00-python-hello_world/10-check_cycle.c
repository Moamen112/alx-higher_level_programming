#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the head of the list
 * 
 * Return: 1 if there is a cycle, 0 otherwise 
 */

int check_cycle(listint_t *list)
{
	listint_t *move_one, *move_two;

	if (list == NULL)
		return (0);

	move_one = list;
	move_two = list->next;

	if (move_two != NULL && move_two->next != NULL)
	{
		if (move_two == move_one)
			return (1);

		move_one = move_one->next;
		move_two = move_two->next->next;
	}

	return (0);
}
