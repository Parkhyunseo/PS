#include<iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    for(int i=N-1; i >=0 ; i--)
    {
        for(int j=0; j < i; j++)
            printf(" ");
        for(int k=i; k < N; k++)
            printf("*");
        printf("\n");
    }
    
}