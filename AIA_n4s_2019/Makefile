##
## EPITECH PROJECT, 2019
## Makefile
## File description:
## Makefile
##

SRC		=		src/main.c			\
				src/getnextline.c	\
				src/get_command.c	\
				src/get_speed.c		\
				src/get_direction.c

CFLAGS          =       -Wall -Wextra -I./include/

OBJ		=	$(SRC:.c=.o)

LIB	=	-L./lib/my/ -lmy

NAME	=	ai

all: 	$(NAME)

$(NAME):	$(OBJ)
		make -C ./lib/my/
		gcc -o $(NAME) $(SRC) $(CFLAGS) $(LDFLAGS) $(LIB)

clean:
		rm -f $(OBJ)
		make clean -C lib/my/

fclean: clean
		make fclean -C lib/my
		rm -f $(NAME)

re:		fclean all
