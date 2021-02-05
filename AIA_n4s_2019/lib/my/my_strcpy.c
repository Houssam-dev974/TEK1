/*
** EPITECH PROJECT, 2019
** my_strcpy
** File description:
** a function
*/

void my_putchar(char c);

char *my_strcpy(char *src, char *dest)
{
    int i = -1;

    while (src[++i])
        dest[i] = src[i];
    return (dest);
}