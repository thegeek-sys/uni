#include <stdio.h>

int main() {
	int n;
	int i = 0;
	int curr;
	int totale = 0;
	scanf("%d", &n);
	while (i<n) {
		do {
			scanf("%d", &curr);
		} while (curr < 0 || curr>10);
		totale += curr;
		i+=1;
	}
	printf("Totale: %d\n", totale);
	printf("Media: %f\n", (float)(totale/n));
	return 1;
}
