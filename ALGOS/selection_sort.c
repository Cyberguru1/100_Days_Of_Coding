#include <stdio.h>
#include <stdlib.h>

void selection_sort(int *array, size_t size);
void swap_func(int **array, size_t a, size_t b);
void print_array(int *array, size_t n);

int main(void)
{
    int array[] = {4,5,6,7,74,44,3};

    size_t n = sizeof(array) / sizeof(array[0]);

    selection_sort(array, n);
    print_array(array, n);
    return (0);
}

/**
 * swap_func - fucntion to swap two values
 * @a: first element
 * @b: second element
 * Return: returns void or none
 */

void swap_func(int **array, size_t a, size_t b)
{
    int temp = (*array)[a];
    (*array)[a] = (*array)[b];
    (*array)[b] = temp;
}

/**
 * selection_sort - function to sort a list
 * @array: array to sort
 * Return: returns void
 */
void selection_sort(int *array, size_t size)
{
    size_t i = 0,j;
    int min,min_index, flag;

    while (i < size)
    {
        j = i + 1;
        min = array[i];
        min_index = i;
        flag = 0;
        while (j < size)
        {
            if (min > array[j])
            {
                min = array[j];
                flag = 1;
                min_index = j;
            }
            j++;
        }

        if (flag)
        {
            swap_func(&array, i, min_index);
        }
        i++;
    }
}
/**
 * print_array - Prints an array of integers
 *
 * @array: The array to be printed
 * @size: Number of elements in @array
 */
void print_array(int *array, size_t n)
{
	size_t i;

	i = 0;
	while (array && i < n)
	{
		if (i > 0)
			printf(", ");
		printf("%d", array[i]);
		++i;
	}
	printf("\n");
}