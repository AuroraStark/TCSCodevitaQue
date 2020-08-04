#include<stdio.h>
#include<math.h>
void func()
{
    double p,s,mi,sum,emi,bank[5],sq;
    int y,n,k,i,yrs,l=0;
    scanf(" %lf",&p);
    scanf(" %d",&y);
    for(k=0;k<2;k++)
    {
    scanf(" %d",&n);
    sum=0;
    for(i=0;i<n;i++)
    {
          scanf(" %d",&yrs);
          scanf(" %lf",&s);
          mi=0;
          sq=pow((1+s),yrs*12);
          emi= (p*(s))/(1-1/sq);
          sum= sum + emi;
     }
     bank[l++]=sum;
    }
    if(bank[0]<bank[1])
        printf("Bank A\n");
    else
        printf("Bank B\n");
}
int main(){
    int k;
    scanf("%d",&k);
    for(int i=0;i<k;i++)
        func();
    return 0;
}
