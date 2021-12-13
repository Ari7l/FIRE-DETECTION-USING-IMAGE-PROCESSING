#include<stdio.h>

int main()
{  

  int rows;
  printf("enter the number of rowa you want");
  scanf("%d",&rows);
  starPattern(rows);
  return 0;

}


void starPattern(int rows)
{
 for(i=0;i<rows;i++)
   {
    for(j=0;j<=i;j++)
    {
     printf("*");
    }
    printf("\n");
   }
}