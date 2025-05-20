#include <stdio.h>
/*** NOTA modificato per fare vedere che la close va in errore
 * va usata la fclose ***/
int main() {


  char str [80];
  float f;
  FILE * pFile;

  pFile = fopen ("myfile.txt","w+");
  fprintf (pFile, "%f %s\n", 3.1416, "PI");
  //close(pFile); // per i file stream FILE bisogna usare la fclose
  //perror("Close");
  rewind (pFile);
  fscanf (pFile, "%f", &f);
  fscanf (pFile, "%s", str);
  //devo conoscere la struttura del file

  //fclose(pFile);
  printf ("I have read: %f and %s \n",f,str);

  pFile = fopen("myfile.txt","r");
  fclose(pFile);
return 0;

}
