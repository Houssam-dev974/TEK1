/*
** EPITECH PROJECT, 2020
** my_getnbr
** File description:
** my_getnbr
*/

int	my_getnbr(char *str)
{
    int	count = 1;
    int	i = 0;
    int	nb = 0;

    while (str[i] != '\0' && (str[i] == '+' || str[i] == '-'))
    {
        if (str[i] == '-')
        count = count * -1;
        i++;
    }
    while (str[i] >= '0' && str[i] <= '9')
    {
        nb = nb * 10;
        nb = nb + (str[i] - '0');
        if (nb < 0)
        if (nb != -2147483648 || count == 1)
            return (0);
        i++;
    }
    return (nb * count);
}