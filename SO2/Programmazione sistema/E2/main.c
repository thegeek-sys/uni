/*
 * Scrivere un programma che prima alloca un area
di memoria, e poi la rialloca ripetutamente con realloc per
aumentarne ogni volta le dimensioni. Verificare se il puntatore
iniziale dell’area di memoria e’ sempre lo stesso oppure
cambia. Trovare un modo per farlo cambiare!!!
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
	char *test = NULL;
	test = malloc(10*sizeof(char));
	printf("%p\n", test);
	//int *trash = malloc(10000);
	for (int i=20;i<100;i+=10) {
		char *new_test = (char *)realloc(test, i*sizeof(char));
		if (test!=new_test) {
			printf("reallocated");
		}
		printf("%p\n", new_test);
		test = new_test;
	}
	free(test);
	return 1;
}
