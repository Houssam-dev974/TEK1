/*
** EPITECH PROJECT, 2020
** main
** File description:
** ai
*/

<<<<<<< HEAD
int run_car(void)
{
    my_putstr("START_SIMULATION");
=======
#include "../include/my.h"

char *check_array(char *str)
{
    int	i = 0;
    int j = 0;
    char *array;
    array = malloc(sizeof(char *) * READ_SIZE);
    if (array == NULL)
        return (NULL);
    while (i != 3)
    if (str[j++] == ':')
        i++;
    i = 0;
    while (str[j] != 0) {
        if ((str[j] >= '0' && str[j] <= '9') ||
        str[j] == '.' || str[j] == ':') {
            array[i] = str[j];
            i++;
        }
        j++;
    }
    array[i - 1] = '\0';
    return (array);
}

void direction_condition(char *str, char **tab, int middle_distance)
{
    my_putstr("get_info_lidar\n");
    str = get_next_line(0);
    detect_stop_car(str);
    str = check_array(str);
    tab = str_to_word_array(str, ":");
    middle_distance = my_getnbr(tab[15]);
}

int	my_car_loop(void)
{
    char **tab;
    char *str;
    int middle_distance;

    while (1)
    {
        my_putstr("get_info_lidar\n");
        str = get_next_line(0);
        detect_stop_car(str);
        str = check_array(str);
        tab = str_to_word_array(str, ":");
        middle_distance = my_getnbr(tab[15]);
        if (car_speed(middle_distance) == 1)
            break;
        direction_condition(str, tab, middle_distance);
        if (car_direction(tab, middle_distance) == 1)
            break;
    }
>>>>>>> 126a3bac1831d496ca12d05d7e34e21c3b3f9952
    return (0);
}

int main(void)
{
<<<<<<< HEAD
    run_car();
=======
    my_command("START_SIMULATION\n");
    my_car_loop();
>>>>>>> 126a3bac1831d496ca12d05d7e34e21c3b3f9952
    return (0);
}