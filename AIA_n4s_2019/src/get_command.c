/*
** EPITECH PROJECT, 2020
** command
** File description:
** cmd
*/

#include "../include/my.h"

int	my_command(char *str)
{
    my_putstr(str);
    str = get_next_line(0);
    if (detect_stop_car(str) == 1)
        return (1);
    return (0);
}

int	detect_stop_car(char *str)
{
    int i = my_strlen(str) - 1, j = 0;
    char *new;
    new = malloc(sizeof(char *) * my_strlen(str));
    if (new == NULL)
        return (-1);
    while (str[i] != ':' && str[i] != 0)
        i -= 1;
    i -= 1;
    while (str[i] != ':' && str[i] != 0)
        i -= 1;
    i += 1;
    while (str[i] != ':' && str[i] != 0)
        new[j++] = str[i++];
    new[j] = 0;
    if (my_strcmp("Track Cleared", new) == 0) {
        free(new);
        my_command("STOP_SIMULATION\n");
        return (1); }
    free(new);
    return (0);
}
