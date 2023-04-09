# include <stdio.h>
void main(){
    int a=0,b=1,c=a+b,number,i;
    printf("Enter Number of lenght you want: ");
    scanf("%d",&number);
    for ( i = 0; i < number; i++)
    {
        printf("%d", c);
        b=a;
        a=c;
        c= a+b;
    }
    

}