##
## EPITECH PROJECT, 2019
## Makefile
## File description:
## Makefile
##

SRC		=	my_putchar.c 		\
			my_putstr.c 		\
			my_strlen.c 		\
			my_getnbr.c			\
			my_strcpy.c			\
			my_strncpy.c			\
			my_strdup.c			\
			my_strcmp.c			\
			my_str_to_word_array.c

CFLAGS		=	-Wall -Wextra -I../../include/
OBJ		=	$(SRC:.c=.o)

HEAD    =   my.h

NAME	=	libmy.a

all: 	$(NAME)

$(NAME):		$(OBJ)
		ar rc $(NAME) $(OBJ)

clean:
		rm -f $(OBJ)

fclean: clean
		rm -f $(NAME)

re:		fclean all
