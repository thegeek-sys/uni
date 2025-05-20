#include <stdio.h>

int main() {
	int n, curr,i=0, totale=0;
	scanf("%d", &n);
	while (i<n) {
		scanf("%d", &curr);
		while (curr < 0 || curr > 10) {
			printf("Valore non ammesso\n");
			scanf("%d", &curr);
		}
		totale += curr;
		i++;
	}
	printf("Totale: %d\n", totale);
	printf("Media: %f\n", (float)(totale/n));
	return 1;
}
