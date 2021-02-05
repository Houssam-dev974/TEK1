/*
** EPITECH PROJECT, 2019
** my_strlen
** File description:
** A function which calculate the length of a string
*/

void my_putchar(char c);

int my_strlen(char const *str)
{
    int i;
    i = 0;
    while (str[i] != '\0')
    {
        i++;
    }
    return (i);
}
