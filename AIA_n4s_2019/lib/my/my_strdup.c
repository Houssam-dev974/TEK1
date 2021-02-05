/*
** EPITECH PROJECT, 2020
** my_strdup
** File description:
** str
*/

#include "my.h"

char *my_new_str(size_t size)
{
    char *str;
    size_t i = 0;
    size_t n = size + 1;

    str = (char *)malloc(sizeof(char) * size + 1);
    if (!str)
        return (NULL);
    if (!n)
        return (NULL);
    while (i < n)
        *(str + i++) = 0;
    return (str);
}

char *my_strdup(const char *s1)
{
    char *tmp;
    size_t n = my_strlen(s1);

    if (!(tmp = my_new_str(n)))
        return (NULL);
    my_strncpy(tmp, s1, n);
    return (tmp);
}

char *my_strchrnul(char *s, int c)
{
    if (!s)
        return (NULL);
    while (*s) {
        if (*s == c)
            break;
        s++;
    }
    return (s);
}