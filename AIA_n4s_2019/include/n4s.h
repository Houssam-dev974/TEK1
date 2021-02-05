/*
** EPITECH PROJECT, 2019
** n4s.h
** File description:
** header
*/

#define READ_SIZE (10000)

char *get_next_line(int fd);
int	car_speed(int middle_distance);
int	car_direction(char **tab, int middle_distance);
int	my_command(char *str);
int	detect_stop_car(char *str);