/*
** EPITECH PROJECT, 2020
** main
** File description:
** ai
*/

#include "../include/my.h"

char *my_buffer(char *buffer, int j, int len)
{
    while (j < (len + READ_SIZE + 1)) {
        buffer[j] = '\0';
        j++;
    }
    return (buffer);
}

char *re_malloc(char *src)
{
    char *dest = malloc(my_strlen(src) + READ_SIZE + 1);
    int	i = 0;

    if (dest == NULL)
        return (NULL);
    while (src[i] != '\0') {
        dest[i] = src[i];
        i++;
    }
    dest = my_buffer(dest, i, my_strlen(src));
    free(src);
    return (dest);
}

char *my_cpy(char *dest, char *src, int *i, int *j)
{
    while (src[*j] == '\n')
        *j = *j + 1;
    while (src[*j] != '\0' && src[*j] != '\n') {
        dest[*i] = src[*j];
        *i = *i + 1;
        *j = *j + 1;
    }
    dest = re_malloc(dest);
    return (dest);
}

char *get_next_line(int fd)
{
    char *str = malloc(READ_SIZE + 1);
    int i = 0;
    static int ret = 1, j = READ_SIZE;
    static char	buffer[READ_SIZE + 1];
    if ((str == NULL) || READ_SIZE == 0)
        return (NULL);
    str = my_buffer(str, 0, 0);
    while (ret > 0 && buffer[j] != '\n') {
        if (buffer[j] == '\0') {
            my_buffer(buffer, 0, 0);
            if (((ret = read(fd, buffer, READ_SIZE)) <= 0)
            && my_strlen(str) <= 0)
                return (NULL);
            j = 0; }
        else if (ret > 0) {
            str = my_cpy(str, buffer, &i, &j);
            if (str == NULL)
                return (NULL); } }
    j++;
    return (str);
}