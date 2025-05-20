#include <stdio.h>
#include "hello_world2.c"

int f(int argc, char *args[]) 
{
  int i = 0;
  printf("Hello World!\n");
  for (i = 0; i < argc; i++)
    printf("L'argomento %d-esimo e' %s\n", i, args[i]);
  return 256;
}

/*[val0, val1, val2, .... valn]
[0     1     2           n]

[helloworld] args[0]
[0] argc=1
*/

