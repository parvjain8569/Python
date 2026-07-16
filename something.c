#include <stdio.h>

int main(){
    int age=20;
    int *ptr=&age;
    printf("%u\n",ptr);
    printf("%p",ptr);
    return 0;
}