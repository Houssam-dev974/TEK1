/*
** EPITECH PROJECT, 2020
** my_strncpy
** File description:
** str
*/

#include "my.h"

char *my_strncpy(char *dst, const char *src, size_t len)
{
    size_t i;

    i = -1;
    while (++i < len)
        if (*(src + i))
            *(dst + i) = *(src + i);
        else
            while (i < len)
                *(dst + i++) = '\0';
    return (dst);
}