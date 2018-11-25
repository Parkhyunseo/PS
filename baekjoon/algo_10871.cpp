#include<iostream>

int main()
{
    int N, X;
    int count= 0;
    int result[10000] = {0};
    scanf("%d %d", &N, &X);
    
    for(int i=0; i < N ;i++){
        int temp;
        scanf("%d", &temp);
        if (temp < X)
            result[count++] = temp;
    }
    
    for(int i=0; i < count ;i++){
        printf("%d ", result[i]);
    }
}