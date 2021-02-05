/*
** EPITECH PROJECT, 2019
** my_putchar
** File description:
** a function
*/

#include<unistd.h>

void my_putchar(char c)
{
    write(1, &c, 1);
}
