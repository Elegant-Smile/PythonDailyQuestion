#include <stdio.h>
#define PEOPLES 10
int main(void) {
    int i;
    int count=0;
    char gender=0;
    int age=-1;
    int numbers=0;
    while(1){
        if (numbers==PEOPLES) break;

        printf("please input your gender(f:feman,m:man)\n");
        scanf("%c",&gender);
        while(getchar()!='\n') continue;
        if((gender!='f')&&(gender!='m')){
            printf("your gender is illegal\n");
            continue;
        }

        printf("please input your age\n");
        scanf("%d",&age);
        while(getchar()!='\n') continue;

        if((age<0)||(130<=age)){
            printf("your age is illegal\n");
            continue;
        }
        numbers+=1;

        if ((gender=='f')&&((10<=age)&&(age<=12))){
            count+=1;
            printf("Congratulation,you can jion in us\n");
        }else{
            printf("Sorry,we need femal and that her age is (10,12)\n");
        }
    }
    printf("%d in our Standard",count);
}
