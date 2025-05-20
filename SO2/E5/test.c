#include <stdio.h>

int main() {
	int num1 = 55;
	int num2 = 30;
	int sum = num1 + num2;
	int printCount;
	printCount = printf("%d + %d = %d\n", num1, num2, sum);
	printf("%d", printCount);
	scanf("%d", &num1);
	printf("%d", num1);

	return 0;
}
