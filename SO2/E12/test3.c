#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	int a, n, count, somma=0;
	if (argc > 2) {
		return 1;
	}
	n = (int)atoi(argv[1]);
	for (count=0;count<n;count++) {
		do {
			printf("Inserisci un numero: ");
			scanf("%d", &a);
		} while (a<=0 || a>=10);
		somma += a;
	}
	printf("Somma: %d\n", somma);
	float media = (float)somma/(float)n;
	printf("Media: %.2f\n", media);
	return 0;
}
