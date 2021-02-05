/*
** EPITECH PROJECT, 2019
** my.h
** File description:
** header
*/

#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include "n4s.h"

void    my_putchar(char);
int     my_putstr(char const *);
int     my_strlen(char const *);
int     my_getnbr(char const *str);
char    **str_to_word_array(char *src, const char *delim);
char    *my_strchrnul(char *s, int c);
char    *my_strdup(const char *s1);
int     my_strcmp(const char *s1, const char *s2);
char    *my_strcpy(char *src, char *dest);
char    *my_strncpy(char *dst, const char *src, size_t len);