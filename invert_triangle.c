# include <stdio.h>
int main () {
    int i,j,num;
    printf("Enter no of stars you want: ");
    scanf("%d",&num);
    printf("printing stars.....\n");
    for (i=0;i<=num;i++)
    {
        for (j=1;j<=i;j++)
        {
            int a=i;
            printf("%d",a);
        }
        printf("\n");
}
     for (i=0;i<=num;i++)
    {
        for (j=1;j<=i;j++)
        {
            int b=j;
            printf("%d",  j);
        }
        printf("\n");
}


}