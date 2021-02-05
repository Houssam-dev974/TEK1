/*
** EPITECH PROJECT, 2020
** direction
** File description:
** dir
*/

#include "../include/my.h"

int	turn_car(int diff, char *val)
{
    my_putstr("wheels_dir:");
    if (diff < 0.0)
        my_putchar('-');
    my_putstr(val);
    val = get_next_line(0);
    if (detect_stop_car(val) == 1)
        return (1);
    return (0);
}

int car_direction(char **tab, int middle_distance)
{
    int left = my_getnbr(tab[1]);
    int right = my_getnbr(tab[31]);
    int diff = left - right;

    switch (middle_distance) {
    case 1000 ... 1499:
        return (turn_car(diff, "0.05\n"));
    case 600 ... 999:
        return (turn_car(diff, "0.1\n"));
    case 400 ... 599:
        return (turn_car(diff, "0.2\n"));
    case 200 ... 399:
        return (turn_car(diff, "0.3\n"));
    default:
        if (middle_distance >= 1500)
            return (turn_car(diff, "0.005\n"));
        else
            return (turn_car(diff, "0.5\n"));
    }
}