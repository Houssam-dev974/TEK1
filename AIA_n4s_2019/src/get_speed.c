/*
** EPITECH PROJECT, 2020
** speed
** File description:
** speed
*/

#include "../include/my.h"

int car_speed(int middle_distance)
{
    switch (middle_distance) {
    case 1500 ... 1999:
        return (my_command("car_forward:0.8\n"));
    case 1000 ... 1499:
        return (my_command("car_forward:0.5\n"));
    case 600 ... 999:
        return (my_command("car_forward:0.4\n"));
    case 400 ... 599:
        return (my_command("car_forward:0.2\n"));
    default:
        if (middle_distance >= 2000)
            return (my_command("car_forward:1.0\n"));
        else
            return (my_command("car_forward:0.1\n"));
    }
}