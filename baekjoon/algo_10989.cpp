#include<iostream>

int count[10001];
int N;

int main()
{
    scanf("%d", &N);
    
    for(int i=0; i < N; i++)
    {
        int c;
        scanf("%d", &c);
        count[c] += 1;
    }
    
    for(int i=1; i <= 10000; i++)
    {
        while(count[i] > 0)
        {
            printf("%d\n", i);
            count[i] -= 1;
        }
    }
        
}